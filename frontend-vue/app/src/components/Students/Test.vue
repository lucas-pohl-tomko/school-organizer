<template>
  <v-card>
    <v-card-title>
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
      :items="schedule"
      :search="search"
    ></v-data-table>
  </v-card>
</template>



<script>
import axios from "axios";
import router from "@/router/"
import CreateStudent from "./Create";

export default {
  name: "Test",
  data() {
    return {
      students: [],

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
        schedule: [
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