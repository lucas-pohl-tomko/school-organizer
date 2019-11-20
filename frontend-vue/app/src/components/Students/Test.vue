<template>
  <v-card>

    <v-card-title>
      <div v-for="x in schedules" v-bind:key="x.id">
        id student: {{x.student}} id professor: {{x.professor}} id schedule: {{x.schedule}}
      </div>
      Horarios 
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="search"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      
      :headers="headers"
      :items="table"
      :search="search"
    ></v-data-table>
  </v-card>
</template>
  



<script>
import axios from "axios";
import router from "@/router/"

export default {
  name: "Test",
  data() {
    return {

      schedules: [],
      search: '',
        headers: [
          {
            text: 'h̵̨̢̡̧̫̳̩̝̜͖̞̼̦̳͖̭̹͉̼̞̺̩̣̝̻̥̘̤̥̜̓͌̒̃̒͋͌̽͋̒̈̄͐̿͗̋͋̈́̍̓̕͝͠o̶̬̯̥̓͒̽̋͒̈́͠ͅr̵̡̪͇̞̯̙̼̪̞̜̮̦͉̳̈̒́̄́̔̆̃̍̏̕͘͝͝ͅͅa̵̡̨̡̻͔̤̲̲͉͓̥̦̼͖̦̖̮̱͕̗̟̭͕͕̦̘̦̙̭͉̮̼͔̣̥̞̠̎͗̚ŗ̵͍̪̦͓͉̟̝̮̳̩̭̑̀̈́̂̍̀̽̕i̷̢̖̖̻̼͔̘̭͚̤͚̮̭͕͔̯̠̼̰͖̝̮̿́͒o̸̡̡̡͖̫̗̬̜͓͍̺̤̬̱͙̘̯̱͇̺͕͔̫̟͈͈̯̦͈͔͕̗̖̒̎̉̀́̇̾͘͘͜͜ͅş̸̧̡̛̰͉̦̤̪̪̘̭̘̗̠̖̫͖̘̰̘̣̙̱̭̯͖̳̗̼̜̳̠̈́̅̆͛̓̌̈́̏̔͑̃́̾̉̄̀̿͋̊̉̏͑͘͘̚͜͝͝͝͝ͅ',
            align: 'left',
            sortable: false,
            value: 'name',
          },
          { text: 'Segunda', value: 'monday' },
          { text: 'Terca', value: 'tuesday' },
          { text: 'Quarta', value: 'wednesday' },
          { text: 'Quinta', value: 'thursday' },
          { text: 'Sexta', value: 'friday' },
          { text: 'Sabado', value: 'saturday' },
        ],
        table: [
          {
            name: '13:00',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
          },
          {
            name: '13:30',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
          },
          {
            name: '14:00',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",         
          },
          {
            name: '14:30',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
},
          {
            name: '15:00',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
          },
          {
            name: '15:30',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",      
          },
          {
            name: '16:00',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
          },
          {
            name: '16:30',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",        
          },
          {
            name: '17:00',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
          },
          {
            name: '17:30',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
          },
          {
            name: '18:00',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
          },
          {
            name: '18:30',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
          },
          {
            name: '19:00',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
          },
          {
            name: '19:30',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
          },
          {
            name: '20:00',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
          },
          {
            name: '20:30',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
          },
          {
            name: '21:00',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
          },
          {
            name: '21:30',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
          },
          {
            name: '22:00',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
          },
          {
            name: '22:30',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
          },
          {
            name: '23:00',
            monday: "maria",
            tuesday: "jose",
            wednesday: "joao",
            thursday: "joaozinho",
            friday: "joel",
            saturday: "aluno teste",
          },
        ],

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
  }
};
</script>