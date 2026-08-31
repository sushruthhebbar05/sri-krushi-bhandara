import React from 'react'
import { useTranslation } from 'react-i18next'
import { useProducts } from '../hooks/useAPI'

export function FeaturedProducts() {
  const { t } = useTranslation()
  const { fetchProducts, products, loading } = useProducts()

  React.useEffect(() => {
    fetchProducts(undefined, undefined, true)
  }, [])

  if (loading) return <div className="text-center py-12">Loading products...</div>

  return (
    <section className="py-16 bg-white">
      <div className="container">
        <h2 className="text-3xl font-bold mb-12 text-center text-krushi-green">
          Featured Products
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {products.slice(0, 4).map((product: any) => (
            <div key={product.id} className="bg-krushi-gray-bg rounded-lg overflow-hidden shadow-md hover:shadow-lg transition">
              {product.image_url && (
                <img src={product.image_url} alt={product.name} className="w-full h-40 object-cover" />
              )}
              <div className="p-4">
                <h3 className="font-bold mb-2 text-krushi-dark">{product.name}</h3>
                <p className="text-sm text-gray-600 mb-4">{product.brand}</p>
                <a href={`/products/${product.id}`} className="text-krushi-green hover:text-krushi-yellow font-semibold text-sm">
                  View Details →
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
