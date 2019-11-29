import Vue from 'vue'
import Router from 'vue-router'

import Index from '@/components/Index'
import Login from '@/views/Login'
import Logout from '@/views/Logout'
import ListBooks from '@/components/Books/List'
import EditBook from'@/components/Books/Edit'
import Experiments from '@/components/Experiments'
import ListStudents from '@/components/Students/List'
import ListProfessors from '@/components/Professors/List'
import EditProfessor from'@/components/Professors/Edit'
import EditStudent from'@/components/Students/Edit'
import Schedule from'@/components/Schedules/ScheduleTable'

Vue.use(Router)

export default new Router({
  mode: 'history',
  hash: false,
  routes: [
    {
      path: '/',
      name: 'Schedule',
      component: Schedule
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/logout',
      name: 'Logout',
      component: Logout
    },
    {
      path: '/books',
      name: 'ListBooks',
      component: ListBooks
    },
    {
      path: '/books/edit/:id',
      name: 'EditBook',
      component: EditBook
    },
    {
      path: '/experiments',
      name: 'Experiments',
      component: Experiments
    },
    {
      path: '/students',
      name: 'ListStudents',
      component: ListStudents
    },
    {
      path: '/professors',
      name: 'ListProfessors',
      component: ListProfessors
    },
    {
      path: '/students/edit/:id',
      name: 'EditStudent',
      component: EditStudent
    },
    {
      path: '/professors/edit/:id',
      name: 'EditProfessor',
      component: EditProfessor
    },
    // {
    //   path: '/schedules',
    //   name: 'Schedule',
    //   component: Schedule
    // }
  ]
})
