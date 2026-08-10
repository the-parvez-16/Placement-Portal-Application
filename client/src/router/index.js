import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/auth/Login.vue'
import Home from "@/views/Home.vue";
import Register from "@/views/auth/Register.vue";
import Dashboard from "@/views/Dashboard.vue";
import Profile from "@/views/Profile.vue";
import NotFound from "@/views/error/NotFound.vue";
import UserDetails from "@/views/UserDetails.vue";
import { authState } from "@/store";
import CompaniesList from "@/views/admin/CompaniesList.vue";
import StudentsList from "@/views/admin/StudentsList.vue";
import DrivesList from "@/views/DrivesList.vue";
import ApplicationsList from "@/views/ApplicationsList.vue";
import DriveDetails from "@/components/details/DriveDetails.vue";
import ReviewApplication from '@/views/ReviewApplication.vue';

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home
    },
    {
        path: "/login",
        name: "Login",
        component: Login
    },
    {
        path: "/register",
        name: "Register",
        component: Register,
    },
    {
        path: "/dashboard",
        name: "Dashboard",
        component: Dashboard,
        meta: { requiresAuth: true }
    },
    {
        path: "/profile",
        name: "MyProfile",
        component: Profile,
        meta: { requiresAuth: true }
    },
    {
        path: "/user/:id",
        name: "UserDetails",
        component: UserDetails,
        meta: { requiresAuth: true }
    },
    {
        path: "/drive/:id",
        name: "DriveDetails",
        component: DriveDetails,
        meta: { requiresAuth: true }
    },
    {
        path: "/review/:id",
        name: "ReviewApplication",
        component: ReviewApplication,
        meta: { requiresAuth: true }
    },
    {
        path: "/admin/companies",
        name: "Companies",
        component: CompaniesList,
        meta: { requiresAuth: true, roles: ['admin', 'sudo'] }
    },
    {
        path: "/admin/students",
        name: "Students",
        component: StudentsList,
        meta: { requiresAuth: true, roles: ['admin', 'sudo'] }
    },
    {
        path: "/drives",
        name: "Drives",
        component: DrivesList,
        meta: { requiresAuth: true }
    },
    {
        path: "/applications",
        name: "Applications",
        component: ApplicationsList,
        meta: { requiresAuth: true }
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component: NotFound
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});

router.beforeEach((to, from) => {
    const token = localStorage.getItem("access_token");

    if (to.meta.requiresAuth && !token) {
        return "login"
    }else if(to.meta.roles && !to.meta.roles.includes(authState.value.role)){
        return "dashboard"
    }else if((to.path === '/' || to.path === '/login' || to.path === '/register') && authState.value.isLoggedIn){
        return "dashboard"
    }else {
        return true;
    }
});


export default router;