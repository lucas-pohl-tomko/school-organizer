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
          <span class="headline">Adicionar Aluno</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field v-model="student.first_name" label="Fist Name*" hint="Student's name" required></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-text-field v-model="student.middle_name" label="Middle Name" hint="Student's middle name" required></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-text-field v-model="student.last_name" label="Last Name*" hint="Student's last name" required></v-text-field>
              </v-col>
            </v-row>           
            <v-row class="form-group" v-for="(input,k) in studentprofessors" :key="k">
                
              <v-col cols="7">
                <v-select
                  :items = "professors"
                  item-value = "id"
                  item-text = "first_name"
                  label = "Professors"
                  attach
                  single-line
                  v-model = "input.professor"
                >
                </v-select>
              </v-col>
              <v-col cols="4">
                <v-select
                  :items = "roles"
                  item-value = "id"
                  item-text = "role"
                  label = "Role"
                  attach
                  single-line
                  v-model="input.role"
                >
                </v-select>
              </v-col>
              <v-col cols="1">
                    <v-icon 
                      @click="addprofessor(k)"
                    >mdi-plus</v-icon>
                    <v-icon 
                      @click="removeprofessor(k)"
                      v-show="k || ( !k && studentprofessors.length > 1)">
                       mdi-minus
                    </v-icon>
              </v-col> 
            </v-row>
          </v-container>
          <small>*Obrigatory information</small>
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
  name: "CreateStudent",
  data() {
    return {
      dialog: false,
      student: {},
      professors: [],
      studentprofessors: [{
        professor: "",
        role: 0
      }],
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
  },
  methods: {
    addprofessor(index) {
      this.studentprofessors.push({ name: '', role: ''});
    },
    removeprofessor(index) {
      this.studentprofessors.splice(index, 1);
    },
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
    add() {
      this.student.professors = this.studentprofessors
      axios
        .post("http://localhost:8000/api/students/add/",
          this.student, 
          {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          }
        )
        .then(response => {
          this.dialog = false
          this.$emit('updateStudents')
          this.log.console(response)
        });
    }
  }
};
</script>
