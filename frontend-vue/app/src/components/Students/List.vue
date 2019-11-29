<template>

  <v-container>
   <v-row no-gutters>
      <v-col
        v-for="student in students" 
        v-bind:key="student.id"
        cols="12"
        sm="4"
      >
    <v-card
      class="mx-auto"
      max-width="344"
      outlined
    >
      <v-list-item three-line>
        <v-list-item-content>
          <div class="overline mb-4">Estudante</div>
          <v-list-item-title class="headline mb-1">{{student.first_name}} {{student.last_name}}</v-list-item-title>
          <v-list-item-subtitle>Nome Completo: {{student.first_name}} {{student.middle_name}} {{student.last_name}}</v-list-item-subtitle>
          <div v-for="professor in student.professors" v-bind:key="professor.id">
            <v-list-item-subtitle>Professor: {{professor}}</v-list-item-subtitle>
          </div>        
        </v-list-item-content>
      </v-list-item>

      <v-card-actions>
        <v-btn class="ma-2" text icon color="red lighten-2">
          <v-icon class="delete" @click="deleteStudent(student)"></v-icon>
        </v-btn>
        <v-btn class="ma-2" text icon color="green">
          <v-icon class="edit" @click="editStudent(student)"></v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
    </v-col>
    </v-row>
          <CreateStudents @updateStudents="all"></CreateStudents>
  </v-container>
</template>


<script>
import axios from "axios";
import router from "@/router/"
import CreateStudent from "./Create";

export default {
  name: "ListStudents",
  data() {
    return {
      students: [],
      authenticated: false
    };
  },
  components: {
    CreateStudents: CreateStudent,
  },
  created() {
    this.all();
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
          url: "/api/students/"
        })
        .then(response => {
          this.students = response.data
          console.log(response)
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
    deleteStudent(student) {
      if (confirm("Excluir " + student.first_name)) {
        axios
          .delete(`http://localhost:8000/api/students/${student.id}`, {
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
    editStudent(student) {
      router.push(`/students/edit/${student.id}`)
    }
  }
};
</script>