<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { navbarState } from '@/store';
import StudentDetails from '@/components/details/StudentDetails.vue';
import CompanyDetails from '@/components/details/CompanyDetails.vue';
import api from "@/services/api"

const route = useRoute();
const userId = route.params.id;

const userData = ref(null);
const userRole = ref('');

onMounted(async () => {
    const response = await api.get(`/auth/users/${userId}`);
    userData.value = response.data;
    userRole.value = response.data.role;

    navbarState.value = {
        title: userRole.value === 'student' ? 'Student Profile' : 'Organization Profile',
        showSearch: false,
        showProfileBtn: false,
        showBackBtn: true,
        backRoute: '' 
    };
});
</script>

<template>
  <div class="row justify-content-center w-100 m-0">
      <div class="col-12 col-lg-8">
          
          <StudentDetails v-if="userRole === 'student'" :student="userData" />
          <CompanyDetails v-else-if="userRole === 'company'" :company="userData" />
          
          <div v-else class="text-center mt-5">
              <span class="spinner-border text-primary" role="status"></span>
          </div>

      </div>
  </div>
</template>