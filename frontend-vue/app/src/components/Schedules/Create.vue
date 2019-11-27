<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on }">
        <v-card-text>
          <v-fab-transition>
            <v-btn primary v-on="on" dark relative fixed bottom right fab>
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </v-fab-transition>
        </v-card-text>
      </template>

      <v-card>
        <v-card-title>
          <span class="headline">Adicionar Aula</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-col cols="7">
                  <v-select
                    :items = "students"
                    item-value = "id"
                    label = "Estudante"
                    attach
                    single-line
                    v-model = "schedulestudentprofessors.student"
                  >
                  <template v-slot:selection="data">
                    {{ data.item.first_name }} {{ data.item.last_name }}
                  </template>
                  <template v-slot:item="data">
                    {{ data.item.first_name }} {{ data.item.last_name }}
                  </template>
                  </v-select>
                </v-col>   
              <v-col cols="7">
                <v-select
                  :items = "professors"
                  item-value = "id"
                  item-text = "first_name"
                  label = "Professor"
                  attach
                  single-line
                  v-model = "schedulestudentprofessors.professor"
                >
                  <template v-slot:selection="data">
                    {{ data.item.first_name }} {{ data.item.last_name }}
                  </template>
                  <template v-slot:item="data">
                    {{ data.item.first_name }} {{ data.item.last_name }}
                  </template>
                </v-select>
              </v-col>     
                <v-col cols="7">
                  <v-select
                    :items = "roles"
                    item-value = "id"
                    item-text = "role"
                    label = "Aula"
                    attach
                    single-line
                    v-model="schedulestudentprofessors.role"
                  >
                  </v-select>
                  <v-select
                  :items = "schedules"
                  item-value = "id"
                  item-text = "timeandday"
                  label = "Horario"
                  attach
                  single-line
                  v-model = "schedulestudentprofessors.schedule"
                >
                </v-select>
                </v-col>
            </v-col>    
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <div class="flex-grow-1"></div>
          <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click="add()">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
import axios from "axios"
export default {
  name: "CreateScheduleStudentProfessor",
  data() {
    return {
      dialog: false,
      students: [],
      professors: [],
      schedules: [],
      schedulestudentprofessors: {},

      roles: [
        {id: 0, role: "Guitarra/Violao"},
        {id: 1, role: "Violino"},
        {id: 2, role: "Sopro"},
        {id: 3, role: "Piano/Teclado"}
      ]
    };
  },
  created() {
    this.getProfessors()
    this.getStudents()
    this.getSchedules()
  },
  methods: {

    getRoles() {
    },
    getProfessors() {
      axios
      .request({
        baseURL: "http://localhost:8000",
        method: "get",
        url: "/api/professors/"
      })
      .then(response => {
        this.professors = response.data
        console.log(response)
      });
    },
    getSchedules() {
      axios
      .request({
        baseURL: "http://localhost:8000",
        method: "get",
        url: "/api/schedules/"
      })
      .then(response => {
        this.schedules = response.data
        console.log(response)
      });
    },
    getStudents() {
      axios
      .request({
        baseURL: "http://localhost:8000",
        method: "get",
        url: "/api/students/"
      })
      .then(response => {
        this.students = response.data
        console.log(response)
      });
    },
    add() {
      axios
        .post("http://localhost:8000/api/schedulestudentsprofessor/add/",
          this.schedulestudentprofessors, 
          {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          }
        )
        .then(response => {
          this.dialog = false
          this.$emit('updateScheduleStudentProfessor')
          this.log.console(response)
        });
    }
  }
};
</script>
