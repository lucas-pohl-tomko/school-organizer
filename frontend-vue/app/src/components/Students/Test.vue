<template>
<!-- STUDENTS TABLE -->

  <v-container class="grey lighten-5">
    <v-row no-gutters>
      <template>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            Ș̶̨̡̥̮̗͚͍̥̻̳̖̖͎̈́̃̚̚͝e̶̬̍̇m̴̧̨̝͇͚͖̭̝̦̗̯̞̜͂̿͊̄͋̑͛̇a̵̬͍͓͍̫͇̦̦̋̀͆ͅͅń̵̢̖̰̟̫̬̣̮͎̭͚̟́̅̿͒́͜͜a̶̧̖̳̼̯̙͖̠̭̤̞͈̒̏̀̋̊̂̂̓́̀̕ 
          </v-card>
        </v-col>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            Segunda

          </v-card>
        </v-col>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            Terca

          </v-card>
        </v-col>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            Quarta

          </v-card>
        </v-col>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            Quinta

          </v-card>
        </v-col>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            Sexta

          </v-card>
        </v-col>
        <v-col>
          <v-card 
            class="pa-2"
            outlined
            tile
          >
            Sabado
          </v-card>
        </v-col>

      
      </template>
    </v-row>

<!-- SCHEDULE TABLE (PLZ JESUS HAVE MERCY) -->

    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            13:00
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            13:30
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            14:00
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            14:30
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
                
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            15:00
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            15:30
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            16:00
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            16:30
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            17:00
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            17:30
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            18:00
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            18:30
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            19:00
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            19:30
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            20:00
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            20:30
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            21:00
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            21:30
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            22:00
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            22:30
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
    <v-row no-gutters>
        <v-col>
          <v-card
            class="pa-2"
            outlined
            tile
          >
            23:00
          </v-card>
        </v-col>

      <template v-for="n in 6">
          
            <v-col :key="n">

            <v-card
                class="pa-2"
                outlined
                tile
            >
                pessoa
            </v-card>
            </v-col>

            <v-responsive
            v-if="n === 6"
            :key="`width-${n}`"
            width="100%"
            ></v-responsive>
      </template>
    </v-row>
  </v-container>

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