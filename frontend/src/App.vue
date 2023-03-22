<template>
    <Navbar />
    <div class="container-fluid py-3">
        <h3 class="text-center mb-3">Books List</h3>
        <BooksTable :books="books" />
    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import BooksTable from '@/components/BooksTable.vue'

import { getBooks } from '@/services/books'

export default {
    name: 'App',
    data() {
        return {
            books: []
        }
    },
    mounted() {
        getBooks().then(data => this.books = data)
    },
    components: {
        Navbar,
        BooksTable
    }
}
</script>

<style></style>
