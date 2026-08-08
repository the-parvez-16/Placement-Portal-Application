import { ref } from 'vue';

export const authState = ref({
    isLoggedIn: !!localStorage.getItem('access_token'),
    role: localStorage.getItem('role') || ''
});
