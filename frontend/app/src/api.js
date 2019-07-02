import axios from 'axios';
import { apiUrl } from '@/env';

function authHeaders(token) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}


export const api = {
  async logInGetToken(email, password) {
    const params = new URLSearchParams();
    params.append('username', email);
    params.append('password', password);
    return axios.post(`${apiUrl}/token/auth`, params);
  },
  async createAccount(email, password) {
    const params = new URLSearchParams();
    params.append('username', email);
    params.append('password', password);
    return axios.post(`${apiUrl}/users/`, {email: email, password:password});
  },
  async pingServer() {
    return axios.get(`${apiUrl}/ping`);
  },
  async getNotes(token) {
    return axios.get(`${apiUrl}/notes/`, authHeaders(token));
  },
  async getGetUserProfile(token) {
    return axios.get(`${apiUrl}/users/me`, authHeaders(token));
  },
  async postNote(token) {
    return axios.post(`${apiUrl}/notes/`, {created: new Date().toJSON(), title: 'Untitled'}, authHeaders(token));
  },
  async deleteNote(token, note_id) {
    return axios.delete(`${apiUrl}/notes/${note_id}`, authHeaders(token));
  },
  async putNote(token, note) {
    return axios.put(`${apiUrl}/notes/${note.id}`, note, authHeaders(token));
  },
  async getNote(token, note_id) {
    return axios.get(`${apiUrl}/notes/${note_id}`, authHeaders(token));
  },
}