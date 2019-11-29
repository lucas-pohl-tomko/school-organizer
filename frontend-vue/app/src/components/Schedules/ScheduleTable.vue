<template>
  <v-data-table
    :headers="headers"
    :items="formattedSchedules"
    :search="search"
    sort-by="calories"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-toolbar-title>Horarios de Aulas</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="search"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
      </v-toolbar>
      <CreateStudents @updateScheduleStudentProfessor="all"></CreateStudents>
    </template>
    <template v-slot:item.action="{ item }">
      <v-btn class="mx-2" fab dark x-small color="primary" @click="goToStudent(item.studentid)">
        <v-icon dark>mdi-pencil</v-icon>
      </v-btn>

      <v-btn class="mx-2" fab dark x-small color="red" @click="deleteItem(item)">
        <v-icon dark>delete</v-icon>
      </v-btn>
          
    </template>

  </v-data-table>
  
</template>


<script>
import axios from "axios";
import router from "@/router/"
import CreateStudent from "./Create";

export default {
  name: "Schedule",
  data() {
    return {
      schedules: [],
      search: '',
      days: {
        MONDAY: 'Segunda-feira',
        TUESDAY: 'Tuesday',
        WEDNESDAY: 'Wednesday',
        THURSDAY: 'Thursday',
        FRIDAY: 'Friday',
        SATURDAY: 'Saturday',
      },
      roles:{
          0: 'Guitarra/Violao',
          1: 'Violino',
          2: 'Sopro',
          3: 'Piano/Teclado'
      },
      dialog: false,
      headers: [

        { text: 'Aluno', value: 'student' },
        { text: 'Professor', value: 'professor' },
        { text: 'Horario', value: 'date.time' },
        { text: 'Dia', value: 'date.dayOfTheWeek' },
        { text: 'Aula', value: 'role' },
        { text: 'Actions', value: 'action', sortable: false },
      ],
      editedIndex: -1,
      editedItem: {
        studentname: '',
        professorname: '',
        time: 0,
        day: '',
        role: '',
      },
      defaultItem: {
        studentname: '',
        professorname: '',
        time: 0,
        day: '',
        role: '',
      },
      authenticated: false
    };
    
  },
  components: {
    CreateStudents: CreateStudent,
  },
  computed: {
    formattedSchedules() {
      return this.schedules.map(schedule => {
        schedule.date.dayOfTheWeek = this.days[schedule.date.dayOfTheWeek]
        schedule.role = this.roles[schedule.role]
        return schedule
      })
    },
    formTitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
    },
  },
    created() {
      this.all();
    },
  watch: {
    dialog (val) {
      val || this.close()
    },
  },
  mounted() {
    this.checkAuthenticated();
  },
  methods: {
    all() {
      axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: "/api/schedulestudentsprofessor/"
        })
        .then(response => {
          this.schedules = response.data
        });
      },
    checkAuthenticated() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/login");
      } else {
        this.authenticated = true;
      }
    },


    deleteItem(item) {
      if (confirm("Excluir " + item.student)) {
        axios
          .delete(`http://localhost:8000/api/schedulestudentsprofessor/destroy/${item.id}`, {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          })
          .then(response => {
            this.all()
            console.log(response)
          });
      }
    },
      close () {
        this.dialog = false
        setTimeout(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        }, 300)
      },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.schedules[this.editedIndex], this.editedItem)
        } else {
          this.schedules.push(this.editedItem)
        }
        this.close()
    },
    goToStudent(student){
      router.push(`/students/edit/${student}`)
    },
    goToProfessor(){
      router.push(`/students`)
    },
    
        },
  }
</script>