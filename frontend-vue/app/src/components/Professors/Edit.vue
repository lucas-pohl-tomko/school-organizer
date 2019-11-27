<template>
  <v-container>
    <h1>Edit professor Info</h1>
    <form>
      <v-text-field
        v-model="professor.first_name"
        :error-messages="first_nameErrors"
        :counter="100"
        label="Name"
        required
        @input="$v.professor.fist_name.$touch()"
        @blur="$v.professor.first_name.$touch()"
      ></v-text-field>
      <v-text-field
        v-model="professor.middle_name"
        :error-messages="middle_nameErrors"
        :counter="100"
        label="Middle Name"
        required
        @input="$v.professor.middle_name.$touch()"
        @blur="$v.professor.middle_name.$touch()"
      ></v-text-field>
      <v-text-field
        v-model="professor.last_name"
        :error-messages="last_nameErrors"
        :counter="100"
        label="Last Name"
        required
        @input="$v.professor.last_name.$touch()"
        @blur="$v.professor.last_name.$touch()"
      ></v-text-field>

      <v-btn class="mr-4" @click="submit">Editar</v-btn>
      <v-btn @click="clear">Voltar</v-btn>
    </form>
  </v-container>
</template>

<script>
import axios from "axios"
import route from "@/router/"
import { validationMixin } from 'vuelidate'

import { required, maxLength } from 'vuelidate/lib/validators'

export default {
  name: 'EditProfessor',
  created () {
    this.getProfessorInfo()
  },
  mixins: [validationMixin],

  validations: {
    professor: {
      first_name: {
        maxLength: maxLength(100),
        required
      },
      middle_name: {
        maxLength: maxLength(100),
      },
      last_name: {
        maxLength: maxLength(100),
        required
      },
    }
  },

  data () {
    return {
      first_name: "",
      middle_name: "",
      last_name: "",
      professor: {}
    }
  },
  computed: {
    first_nameErrors () {
      const errors = []
      if (!this.$v.professor.first_name.$dirty) return errors
      !this.$v.professor.first_name.maxLength && errors.push('Name must be at most 100 characters long')
      !this.$v.professor.first_name.required && errors.push('Name is required.')

    },
    middle_nameErrors () {
      const errors = []
      if (!this.$v.professor.middle_name.$dirty) return errors
      !this.$v.professor.middle_name.maxLength && errors.push('Middle Name must be at most 100 characters long')
      return errors
    },
    last_nameErrors () {
      const errors = []
      if (!this.$v.professor.last_name.$dirty) return errors
      !this.$v.professor.last_name.maxLength && errors.push('Last Name must be at most 100 characters long')
      !this.$v.professor.last_name.required && errors.push('Last Name is required.')
      return errors
    },
  },
  methods: {
    getProfessorInfo() {
      axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: `/api/professors/get/${this.$route.params.id}/`
        })
        .then(res => {
          this.professor = res.data
          console.log(res)
        });
    },
    submit () {
      axios
        .put(
          `http://localhost:8000/api/professors/edit/${this.$route.params.id}/`,
          this.professor, 
          {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          }
        )
        .then(res => {
          route.push('/professors/')
          console.log(res)
        });
    },
    clear () {
      route.push('/professors/')
    },
  }
}
</script>