import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/auth/Login.vue'
import Home from "@/views/Home.vue";
import Register from "@/views/auth/Register.vue";
import Dashboard from "@/views/Dashboard.vue";
import NotFound from "@/views/error/NotFound.vue";

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
    }
    else {
        return true;
    }
});


export default router;