import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import '@/assets/css/tailwind.css'
import { library } from '@fortawesome/fontawesome-svg-core'
import { 
  faCoffee, 
  faBold, 
  faItalic, 
  faStrikethrough, 
  faUnderline, 
  faCode, 
  faParagraph, 
  faListOl, 
  faListUl,
  faQuoteRight,
  faFileCode,
  faRulerHorizontal,
  faUndo,
  faRedo,
  faSpinner,
  faAngleLeft,
  faAngleRight,
  faTrash,
  faTimes
} from '@fortawesome/free-solid-svg-icons'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(
  faCoffee, 
  faBold, 
  faItalic, 
  faStrikethrough, 
  faUnderline, 
  faCode, 
  faParagraph, 
  faListOl, 
  faListUl,
  faQuoteRight,
  faFileCode,
  faRulerHorizontal, 
  faUndo,
  faRedo,
  faSpinner,
  faAngleLeft,
  faAngleRight,
  faTrash,
  faTimes
  )

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
