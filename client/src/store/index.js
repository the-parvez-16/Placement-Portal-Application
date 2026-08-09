import { ref } from 'vue';

export const authState = ref({
    isLoggedIn: !!localStorage.getItem('access_token'),
    role: localStorage.getItem('role') || ''
});

export const alertState = ref({
    type:"",
    message:""
})

export const navbarState = ref({
    title: 'Placement Portal',
    showSearch: false,
    searchQuery: '',
    searchPlceholder: '',
    showBackBtn: false,
    backText: '← Back to Dashboard',
    backRoute: '/dashboard',
    showProfileBtn: false,
    profileRoute: '/profile'
});
