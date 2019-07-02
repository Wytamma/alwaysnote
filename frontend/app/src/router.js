import Vue from 'vue'
import Router from 'vue-router'
import ErrorVue from './views/Error.vue'
import Login from '@/components/auth/Login.vue'
import New from '@/components/auth/New.vue'
import Forgot from '@/components/auth/Forgot.vue'
import store from './store'

Vue.use(Router)

let router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/auth',
      redirect: '/auth/login',
      component: () => import(/* webpackChunkName: "auth" */ './views/Auth.vue'),
      children: [
        {
          path: 'login',
          name: 'Login',
          component: Login
        },
        {
          path: 'new',
          name: 'New',
          component: New
        },
        {
          path: 'forgot',
          name: 'Forgot',
          component: Forgot
        },
      ]
    },
    {
      path: '/home',
      name: 'Home',
      component: () => import(/* webpackChunkName: "home" */ './views/Home.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/404',
      name: '404',
      alias: '*',
      component: ErrorVue
    },
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '*',
      redirect: '/404'
    },
  ]
})

// https://github.com/tiangolo/full-stack-fastapi-postgresql/search?q=dispatchCheckLoggedIn&unscoped_q=dispatchCheckLoggedIn

router.beforeEach((to, from, next) => {
  let requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  console.log(to, from)
  console.log('requiresAuth', requiresAuth)
  console.log('isLoggedIn', store.state.isLoggedIn)
  if (requiresAuth && !store.state.isLoggedIn) next({name: 'Login'})
  else if (!requiresAuth && store.state.isLoggedIn) next({name: 'Home'})
  else next()
})

export default router