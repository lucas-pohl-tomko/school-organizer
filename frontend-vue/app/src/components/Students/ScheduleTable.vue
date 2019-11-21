<template>
  <v-simple-table fixed-header height="300px">
     
      <thead>
        <v-card-title>
        Horarios
        <v-spacer></v-spacer>
        </v-card-title>
        <tr>
          <th class="text-left">Aluno</th>
          <th class="text-left">Professor</th>
          <th class="text-left">Horario</th>
          <th class="text-left"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="x in formattedSchedules" :key="x.id">
          <td><a @click=goToStudent()>{{ x.student }}</a></td>
          <td><a @click=goToProfessor()>{{ x.professor }}</a></td>
          <td>{{ x.date.time }}</td>
          <td>{{ x.date.dayOfTheWeek }}</td>
          
          
        </tr>
      </tbody>
  </v-simple-table>
</template>
  



<script>
import axios from "axios";
import router from "@/router/"

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
      }

    };
  },
  computed: {
    formattedSchedules() {
      return this.schedules.map(schedule => {
        schedule.date.dayOfTheWeek = this.days[schedule.date.dayOfTheWeek]
        return schedule
      })
    }
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
          url: "/api/schedulestudentsprofessor/"
        })
        .then(response => {
          this.schedules = response.data
        });
        
      },
    goToStudent(student){
      router.push(`/students`)
    },
    goToProfessor(){
      router.push(`/students`)
    },
    
        },
  }
</script>