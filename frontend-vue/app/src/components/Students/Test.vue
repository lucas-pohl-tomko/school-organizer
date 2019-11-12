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
            tuesday: 6.0,
            wednesday: 24,
            thursday: 4.0,
            friday: '1%',
            saturday: "aluno teste",
          },
          {
            name: '13:30',
            monday: 237,
            tuesday: 9.0,
            wednesday: 37,
            thursday: 4.3,
            friday: '1%',
            saturday: "aluno teste",
          },
          {
            name: '14:00',
            monday: 262,
            tuesday: 16.0,
            wednesday: 23,
            thursday: 6.0,
            friday: '7%',
            saturday: "aluno teste",            
          },
          {
            name: '14:30',
            monday: 305,
            tuesday: 3.7,
            wednesday: 67,
            thursday: 4.3,
            friday: '8%',
            saturday: "aluno teste",
},
          {
            name: '15:00',
            monday: 356,
            tuesday: 16.0,
            wednesday: 49,
            thursday: 3.9,
            friday: '16%',
            saturday: "aluno teste",
          },
          {
            name: '15:30',
            monday: 375,
            tuesday: 0.0,
            wednesday: 94,
            thursday: 0.0,
            friday: '0%',
            saturday: "aluno teste",         
          },
          {
            name: '16:00',
            monday: 392,
            tuesday: 0.2,
            wednesday: 98,
            thursday: 0,
            friday: '2%',
            saturday: "aluno teste",
          },
          {
            name: '16:30',
            monday: 408,
            tuesday: 3.2,
            wednesday: 87,
            thursday: 6.5,
            friday: '45%',
            saturday: "aluno teste",          
          },
          {
            name: '17:00',
            monday: 452,
            tuesday: 25.0,
            wednesday: 51,
            thursday: 4.9,
            friday: '22%',
            saturday: "aluno teste",
          },
          {
            name: '17:30',
            monday: 518,
            tuesday: 26.0,
            wednesday: 65,
            thursday: 7,
            friday: '6%',
            saturday: "aluno teste",
          },
          {
            name: '18:00',
            monday: 518,
            tuesday: 26.0,
            wednesday: 65,
            thursday: 7,
            friday: '6%',
            saturday: "aluno teste",
          },
          {
            name: '18:30',
            monday: 518,
            tuesday: 26.0,
            wednesday: 65,
            thursday: 7,
            friday: '6%',
            saturday: "aluno teste",
          },
          {
            name: '19:00',
            monday: 518,
            tuesday: 26.0,
            wednesday: 65,
            thursday: 7,
            friday: '6%',
            saturday: "aluno teste",
          },
          {
            name: '19:30',
            monday: 518,
            tuesday: 26.0,
            wednesday: 65,
            thursday: 7,
            friday: '6%',
            saturday: "aluno teste",
          },
          {
            name: '20:00',
            monday: 518,
            tuesday: 26.0,
            wednesday: 65,
            thursday: 7,
            friday: '6%',
            saturday: "aluno teste",
          },
          {
            name: '20:30',
            monday: 518,
            tuesday: 26.0,
            wednesday: 65,
            thursday: 7,
            friday: '6%',
            saturday: "aluno teste",
          },
          {
            name: '21:00',
            monday: 518,
            tuesday: 26.0,
            wednesday: 65,
            thursday: 7,
            friday: '6%',
            saturday: "aluno teste",
          },
          {
            name: '21:30',
            monday: 518,
            tuesday: 26.0,
            wednesday: 65,
            thursday: 7,
            friday: '6%',
            saturday: "aluno teste",
          },
          {
            name: '22:00',
            monday: 518,
            tuesday: 26.0,
            wednesday: 65,
            thursday: 7,
            friday: '6%',
            saturday: "aluno teste",
          },
          {
            name: '22:30',
            monday: 518,
            tuesday: 26.0,
            wednesday: 65,
            thursday: 7,
            friday: '6%',
            saturday: "aluno teste",
          },
          {
            name: '23:00',
            monday: 518,
            tuesday: 26.0,
            wednesday: 65,
            thursday: 7,
            friday: '6%',
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