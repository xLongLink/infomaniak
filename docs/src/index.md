---
layout: false
---

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vitepress'

const router = useRouter()

onMounted(() => {
  router.go('/core/')
})
</script>

<meta http-equiv="refresh" content="0; url=/core/">
<link rel="canonical" href="/core/">
