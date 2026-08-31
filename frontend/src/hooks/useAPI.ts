import { useState } from 'react'
import { useTranslation } from 'react-i18next'
import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

export function useCropAnalysis() {
  const { t } = useTranslation()
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [result, setResult] = useState(null)

  const analyzeCrop = async (cropName: string, symptoms: string, location?: string) => {
    setLoading(true)
    setError(null)
    try {
      const response = await axios.post(`${API_URL}/ai/crop-analysis`, {
        crop_name: cropName,
        symptoms,
        location,
      })
      setResult(response.data)
      return response.data
    } catch (err: any) {
      const errorMsg = err.response?.data?.detail || 'Analysis failed. Please try again.'
      setError(errorMsg)
      throw err
    } finally {
      setLoading(false)
    }
  }

  return { analyzeCrop, loading, error, result }
}

export function useChat() {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [conversationId, setConversationId] = useState<string | null>(null)

  const sendMessage = async (message: string, cropContext?: string) => {
    setLoading(true)
    setError(null)
    try {
      const response = await axios.post(`${API_URL}/ai/chat`, {
        message,
        conversation_id: conversationId,
        crop_context: cropContext,
      })
      setConversationId(response.data.conversation_id)
      return response.data
    } catch (err: any) {
      const errorMsg = err.response?.data?.detail || 'Failed to send message'
      setError(errorMsg)
      throw err
    } finally {
      setLoading(false)
    }
  }

  return { sendMessage, loading, error, conversationId }
}

export function useProducts() {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [products, setProducts] = useState([])
  const [total, setTotal] = useState(0)

  const fetchProducts = async (categoryId?: string, crop?: string, featured?: boolean) => {
    setLoading(true)
    setError(null)
    try {
      const params = new URLSearchParams()
      if (categoryId) params.append('category_id', categoryId)
      if (crop) params.append('crop', crop)
      if (featured !== undefined) params.append('featured', String(featured))
      params.append('limit', '50')

      const response = await axios.get(`${API_URL}/products?${params}`)
      setProducts(response.data.items)
      setTotal(response.data.total)
      return response.data
    } catch (err: any) {
      setError('Failed to fetch products')
      throw err
    } finally {
      setLoading(false)
    }
  }

  return { fetchProducts, products, loading, error, total }
}

export function useSearch() {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [results, setResults] = useState<any>(null)

  const search = async (query: string, language: string = 'en') => {
    if (!query.trim()) {
      setResults(null)
      return
    }

    setLoading(true)
    setError(null)
    try {
      const response = await axios.get(`${API_URL}/search?q=${encodeURIComponent(query)}&language=${language}`)
      setResults(response.data)
      return response.data
    } catch (err: any) {
      setError('Search failed')
      throw err
    } finally {
      setLoading(false)
    }
  }

  return { search, results, loading, error }
}
