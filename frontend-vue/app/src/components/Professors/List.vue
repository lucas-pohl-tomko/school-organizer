
<template>

  <v-container>
   <v-row no-gutters>
      <v-col
        v-for="professor in professors" 
        v-bind:key="professor.id"
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
          <div class="overline mb-4">Professor</div>
          <v-list-item-title class="headline mb-1">{{professor.first_name}} {{professor.middle_name}} {{professor.last_name}}</v-list-item-title> 
        </v-list-item-content>
      </v-list-item>

      <v-card-actions>
          <v-btn class="ma-2" text icon color="red lighten-2">
            <v-icon class="delete" @click="deleteProfessor(professor)"></v-icon>
          </v-btn>
          <v-btn class="ma-2" text icon color="green">
            <v-icon class="edit" @click="editProfessor(professor)"></v-icon>
          </v-btn>
      </v-card-actions>
    </v-card>
    </v-col>
    </v-row>
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
      authenticated: false,
    };
  },
  components: {
    CreateProfessor: CreateProfessor,
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
          url: "/api/professors/"
        })
        .then(response => {
          this.professors = response.data
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