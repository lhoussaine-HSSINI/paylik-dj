import axios from "axios"

const apiBaseUrl = "http://localhost:8000/api/"

const axiosBooks = axios.create({
    baseURL: apiBaseUrl + "books"
})

export const getBooks = async () => {
    try {
        const response = await axiosBooks.get("/")
        return response.data
    } catch {
        return []
    }
}
