import Vue from 'vue'
import Vuex from 'vuex'
import { api } from '@/api';
import router from '@/router';
import _ from 'lodash'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: null,
    isLoggedIn: false,
    logInError: false,
    email: null,
    notes: [],
    note: null, // note hold the currecnt state 
    activeNote: null, // activeNote is the starting state upon selection.
    messages: [],
    notesHidden: false,
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
    },
    setLoggedIn(state, payload) {
      state.isLoggedIn = payload;
    },
    setNotes(state, payload) {
      state.notes = payload;
    },
    pushNote(state, payload) {
      state.notes.push(payload);
    },
    setNote(state, payload) {
      state.note = payload;
    },
    setActiveNote(state, payload) {
      state.activeNote = payload;
    },
    setEmail(state, payload) {
      state.email = payload;
    },
    updateNoteInNotes(state, payload) {
      //Find index of specific object using findIndex method.    
      const noteIndex = state.notes.findIndex((note => note.id == payload.id));
      //Update object's name property.
      console.log(noteIndex)
      state.notes[noteIndex] = payload
      Vue.set(state, 'notes', [...state.notes])
    },
    removeMessage(state, index) {
      state.messages.splice(index, 1)
    },
    addMessage(state, payload) {
      console.log(state.messages);
      state.messages.push(payload)
    },
    setNotesHidden(state, bool) {
      state.notesHidden = bool
    }
  },
  getters: {
    orderedNotes: state => {
      return _.orderBy(state.notes, 'updated', 'desc'); // ordered
    },
    activeNote: state => {
      return state.activeNote
    },
  },
  actions: {
    // https://github.com/tiangolo/full-stack-fastapi-postgresql/search?q=dispatchCheckLoggedIn&unscoped_q=dispatchCheckLoggedIn
    // rewrtie as promise
    async actionLogIn(context, {email, password}) {
      try {
          const response = await api.logInGetToken(email, password); // for can catch the 404 with a promise 
          
          const token = response.data.access_token;
          if (token) {
              //saveLocalToken(token);// don't do that
              //commitSetToken(context, token);
              context.commit('setToken', token)
              context.commit('setLoggedIn', true)
              //commitSetLogInError(context, false);
              //await actionGetUserProfile(context);
              await context.dispatch('actionGetUserProfile')
              await context.dispatch('actionRouteLoggedIn')
              //commitAddNotification(context, { content: 'Logged in', color: 'success' });
          } else {
              //need to remove token cookie
              console.log('no token')
              //await dispatchLogOut(context);
          }
      } catch (error) {
          //commitSetLogInError(context, true);
          //need to remove token cookie
          context.dispatch('actionParseError', error)
          
          //await dispatchLogOut(context);
      }
  },
  async actionCreateAccount(context, {email, password}) {
      api.createAccount(email, password)
      .then(response => {
        context.dispatch('actionRouteAccountCreated')
        context.commit('addMessage', "Account Created")
      }).catch(error => {
        context.dispatch('actionParseError', error)
      }) // log is server down
  },
  actionParseError(context, error) {
    if (error.response) {
      if (error.response.status == 422) {
        for (let i = 0; i < error.response.data.detail.length; i++) {
          context.commit('addMessage', error.response.data.detail[i].msg)
        }
      } else {
        context.commit('addMessage', error.response.data.detail)
      }
    } else {
      context.commit('addMessage', error)
    }
  },
  actionRouteLoggedIn(context) {
      router.push({name: 'Home'})
  },
  actionRouteAccountCreated(context) {
    router.push({name: 'Login'})
  },
  actionRouteLoggedOut(context) {
      router.push({name: 'Login'})
  },
  async actionLogOut(context) {
    try {
        // const response = await api.logInGetToken(email, password); // delete cookie
        // if they're offline they can't delete their cookie....
        context.commit('setLoggedIn', false)
        await context.dispatch('actionRouteLoggedOut')
    } catch (err) {
        //commitSetLogInError(context, true);
        console.log(err)
    }
  },
  async actionPingServer(context) {
    api.pingServer()
    .then(response => (console.log(response.data))) // context.dispatch('serverOnline', true)
    .catch(error => console.log(error)) // log is server down
  },
  async actionGetNotes(context) {
    try {
      const response = await api.getNotes(context.state.token); 
      
      const notes = _.orderBy(response.data, 'updated', 'desc'); // ordered
      
      context.commit('setNotes', notes)
      if (notes.length > 0) {
        // set active note to last updated
        await context.dispatch('actionSetActiveNote', notes[0].id)
      } else {
        // no notes 
        context.commit('setActiveNote', null)
        context.commit('setNote', null)
      }
      


  } catch (err) {
      //commitSetLogInError(context, true);
      console.log(err)
      //await dispatchLogOut(context);
  }
  },
  async actionGetUserProfile(context) {
    try {
      const response = await api.getGetUserProfile(context.state.token); 
      const email = response.data.email;
      context.commit('setEmail', email)
    } catch (err) {
        //commitSetLogInError(context, true);
        console.log(err)
        //await dispatchLogOut(context);
    }
  },
  async actionSetActiveNote(context, note_id) {
    // send final update
    var response
    const lastActiveNote = context.getters.activeNote
    if (lastActiveNote) {
      console.log('found last active');
      const response = await api.getNote(context.state.token, lastActiveNote.id); 
      context.commit('updateNoteInNotes', response.data)
    }
    // refresh
    response = await api.getNote(context.state.token, note_id); 
    const note = response.data
    
    context.commit('updateNoteInNotes', note)
    context.commit('setNote', note)
    context.commit('setActiveNote', note)
  },
  async actionRemoveMessage(context, message_index) {
    context.commit('removeMessage', message_index)
  },
  async actionAddMessage(context, message) {
    context.commit('addMessage', message)
  },
  async actionCreateNewNote(context) {
    try {
      const response = await api.postNote(context.state.token); 
      console.log(response.data);
      const note = response.data;
      console.log('berfire pushNote');
      
      await context.commit('pushNote', note)
      console.log('berfire actionSetActiveNote');
      await context.dispatch('actionSetActiveNote', note.id)
      
    } catch (err) {
        //commitSetLogInError(context, true);
        console.log(err)
        //await dispatchLogOut(context);
    }
  },
  async actionUpdateNote(context, note) {
    try {
      console.log(note);
      const response = await api.putNote(context.state.token, note); 
      context.commit('setNote', response.data)
      // refresh notes
    } catch (err) {
        //commitSetLogInError(context, true);
        console.log(err)
        //await dispatchLogOut(context);
    }
  },
  async actionDeleteNote(context, note) {
    try {
      // delete in data base
      const response = await api.deleteNote(context.state.token, note.id); 
      // refresh notes
      context.commit('setActiveNote', null)
      await context.dispatch('actionGetNotes')
    } catch (err) {
        //commitSetLogInError(context, true);
        console.log(err)
        //await dispatchLogOut(context);
    }
  },
  async actionSetNotesHidden(context, bool) {
    context.commit('setNotesHidden', bool)
    console.log('setNotesHidden', bool)
  },
}
})
