<template>
  <v-container>
    <h1>Edit Student Info</h1>
    <form>
      <v-text-field
        v-model="student.first_name"
        :error-messages="first_nameErrors"
        :counter="100"
        label="Name"
        required
        @input="$v.student.fist_name.$touch()"
        @blur="$v.student.first_name.$touch()"
      ></v-text-field>
      <v-text-field
        v-model="student.middle_name"
        :error-messages="middle_nameErrors"
        :counter="100"
        label="Middle Name"
        required
        @input="$v.student.middle_name.$touch()"
        @blur="$v.student.middle_name.$touch()"
      ></v-text-field>
      <v-text-field
        v-model="student.last_name"
        :error-messages="last_nameErrors"
        :counter="100"
        label="Last Name"
        required
        @input="$v.student.last_name.$touch()"
        @blur="$v.student.last_name.$touch()"
      ></v-text-field>

      <v-btn class="mr-4" @click="submit">Submit</v-btn>
      <v-btn @click="clear">Clear</v-btn>
    </form>
  </v-container>
</template>

<script>
import axios from "axios"
import route from "@/router/"
import { validationMixin } from 'vuelidate'

import { required, maxLength } from 'vuelidate/lib/validators'

export default {
  name: 'EditStudent',
  created () {
    this.getStudentInfo()
  },
  mixins: [validationMixin],

  validations: {
    student: {
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
      student: {}
    }
  },
  computed: {
    first_nameErrors () {
      const errors = []
      if (!this.$v.student.first_name.$dirty) return errors
      !this.$v.student.first_name.maxLength && errors.push('Name must be at most 100 characters long')
      !this.$v.student.first_name.required && errors.push('Name is required.')

    },
    middle_nameErrors () {
      const errors = []
      if (!this.$v.student.middle_name.$dirty) return errors
      !this.$v.student.middle_name.maxLength && errors.push('Middle Name must be at most 100 characters long')
      !this.$v.student.middle_name.required && errors.push('Middle Name is required.')
      return errors
    },
    last_nameErrors () {
      const errors = []
      if (!this.$v.student.last_name.$dirty) return errors
      !this.$v.student.last_name.maxLength && errors.push('Last Name must be at most 100 characters long')
      !this.$v.student.last_name.required && errors.push('Last Name is required.')
      return errors
    },
  },
  methods: {
    getStudentInfo() {
      axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: `/api/students/get/${this.$route.params.id}/`
        })
        .then(res => {
          this.student = res.data
          console.log(res)
        });
    },
    submit () {
      axios
        .put(
          `http://localhost:8000/api/students/edit/${this.$route.params.id}/`,
          this.student, 
          {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          }
        )
        .then(res => {
          route.push('/students/')
          console.log(res)
        });
    },
    clear () {
      route.push('/students/')
    },
  }
}
</script>