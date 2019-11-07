<template>
  <v-container>
      <div v-for="student in students" v-bind:key="student.id">
        <p>Aluno: {{student.first_name}} {{student.middle_name}} {{student.last_name}}</p>
        <p>Professor: {{student.professors}}</p>
        
        <v-btn class="ma-2" text icon color="red lighten-2">
          <v-icon class="delete" @click="deleteStudent(student)"></v-icon>
        </v-btn>
        <v-btn class="ma-2" text icon color="green">
          <v-icon class="edit" @click="editStudent(student)"></v-icon>
        </v-btn>
        <v-divider></v-divider>
      </div>
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
    };
  },
  components: {
    CreateStudents: CreateStudent,
  },
  created() {
    this.all();
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