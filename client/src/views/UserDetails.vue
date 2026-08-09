<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { navbarState } from '@/store';
import StudentDetails from '@/components/details/StudentDetails.vue';
import CompanyDetails from '@/components/details/CompanyDetails.vue';

const route = useRoute();
const userId = route.params.id;

// API se aane wala data state
const userData = ref(null);
const userRole = ref(''); // 'student' ya 'company'

onMounted(async () => {
    // API call simulation
    // const response = await api.get(`/users/${userId}`);
    // userData.value = response.data;
    // userRole.value = response.data.role;
    
    // Dummy Data for testing
    userRole.value = 'company'; 
    userData.value = {
        id: userId,
        name: 'Tech Solutions',
        email: 'hr@techsolutions.com',
        status: 'PENDING',
        hr_contact: 'John Doe / +91-9876543210',
        website: 'https://techsolutions.com',
        drives: [
            { id: 1, job_title: 'Software Engineer', salary: '800000' }
        ]
    };

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
  <div class="row justify-content-center w-100">
      <div class="col-12 col-lg-8">
          
          <!-- Render based on role -->
          <StudentDetails v-if="userRole === 'student'" :student="userData" />
          <CompanyDetails v-else-if="userRole === 'company'" :company="userData" />
          
          <div v-else class="text-center mt-5">
              <span class="spinner-border text-primary" role="status"></span>
          </div>

      </div>
  </div>
</template>