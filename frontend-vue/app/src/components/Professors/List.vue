<template>
  <v-container>

        <div v-for="professor in professors" v-bind:key="professor.id">
          <p>Professor: {{professor.first_name}} {{professor.middle_name}} {{professor.last_name}}</p>
          <v-btn class="ma-2" text icon color="red lighten-2">
            <v-icon class="delete" @click="deleteProfessor(professor)"></v-icon>
          </v-btn>
          <v-btn class="ma-2" text icon color="green">
            <v-icon class="edit" @click="editProfessor(professor)"></v-icon>
          </v-btn>
          <v-divider></v-divider>
        </div>

      <CreateProfessor @updateProfessors="all"></CreateProfessor>
  </v-container>
</template>


<script>
import axios from "axios";
import router from "@/router/"
import CreateProfessor from "./Create";

export default {
  name: "ListProfessor",
  data() {
    return {
      professors: [],
    };
  },
  components: {
    CreateProfessor: CreateProfessor,
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
          url: "/api/professors/"
        })
        .then(response => {
          this.professors = response.data
          console.log(response)
        });
    },
    deleteProfessor(professor) {
      if (confirm("Excluir " + professor.first_name)) {
        axios
          .delete(`http://localhost:8000/api/professors/${professor.id}`, {
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
    editProfessor(professor) {
      router.push(`/professors/edit/${professor.id}`)
    }
  }
};
</script>