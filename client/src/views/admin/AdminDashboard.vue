<script setup>
const role = localStorage.getItem('role');
</script>

<template>
  <h1>{{  role.charAt(0).toUpperCase() + role.slice(1) }} Dashboard</h1>
</template>
