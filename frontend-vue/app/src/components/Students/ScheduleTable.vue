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
        </tr>
      </thead>
      <tbody>
        <tr v-for="x in schedules" :key="x.id">
          <td><a v-on:click=goToStudent()>{{ x.student }}</a></td>
          <td><a v-on:click=goToProfessor()>{{ x.professor }}</a></td>
          <td>{{ x.schedule }}</td>
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
      //   headers: [
      //     {
      //       text: 'h̵̨̢̡̧̫̳̩̝̜͖̞̼̦̳͖̭̹͉̼̞̺̩̣̝̻̥̘̤̥̜̓͌̒̃̒͋͌̽͋̒̈̄͐̿͗̋͋̈́̍̓̕͝͠o̶̬̯̥̓͒̽̋͒̈́͠ͅr̵̡̪͇̞̯̙̼̪̞̜̮̦͉̳̈̒́̄́̔̆̃̍̏̕͘͝͝ͅͅa̵̡̨̡̻͔̤̲̲͉͓̥̦̼͖̦̖̮̱͕̗̟̭͕͕̦̘̦̙̭͉̮̼͔̣̥̞̠̎͗̚ŗ̵͍̪̦͓͉̟̝̮̳̩̭̑̀̈́̂̍̀̽̕i̷̢̖̖̻̼͔̘̭͚̤͚̮̭͕͔̯̠̼̰͖̝̮̿́͒o̸̡̡̡͖̫̗̬̜͓͍̺̤̬̱͙̘̯̱͇̺͕͔̫̟͈͈̯̦͈͔͕̗̖̒̎̉̀́̇̾͘͘͜͜ͅş̸̧̡̛̰͉̦̤̪̪̘̭̘̗̠̖̫͖̘̰̘̣̙̱̭̯͖̳̗̼̜̳̠̈́̅̆͛̓̌̈́̏̔͑̃́̾̉̄̀̿͋̊̉̏͑͘͘̚͜͝͝͝͝ͅ',
      //       align: 'left',
      //       sortable: false,
      //       value: 'name',
      //     },
      //     { text: 'Segunda', value: 'monday' },
      //     { text: 'Terca', value: 'tuesday' },
      //     { text: 'Quarta', value: 'wednesday' },
      //     { text: 'Quinta', value: 'thursday' },
      //     { text: 'Sexta', value: 'friday' },
      //     { text: 'Sabado', value: 'saturday' },
      //   ],
      //   table: [
        
      //     {
      //       name: '13:00',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //     {
      //       name: '13:30',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //     {
      //       name: '14:00',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",         
      //     },
      //     {
      //       name: '14:30',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //     {
      //       name: '15:00',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //     {
      //       name: '15:30',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",      
      //     },
      //     {
      //       name: '16:00',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //     {
      //       name: '16:30',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",        
      //     },
      //     {
      //       name: '17:00',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //     {
      //       name: '17:30',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //     {
      //       name: '18:00',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //     {
      //       name: '18:30',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //     {
      //       name: '19:00',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //     {
      //       name: '19:30',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //     {
      //       name: '20:00',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //     {
      //       name: '20:30',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //     {
      //       name: '21:00',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //     {
      //       name: '21:30',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //     {
      //       name: '22:00',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //     {
      //       name: '22:30',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //     {
      //       name: '23:00',
      //       monday: "maria",
      //       tuesday: "jose",
      //       wednesday: "joao",
      //       thursday: "joaozinho",
      //       friday: "joel",
      //       saturday: "aluno teste",
      //     },
      //   ],

    };
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
          console.log(response)
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