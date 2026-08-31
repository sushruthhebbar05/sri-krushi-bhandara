import React from 'react'
import { useTranslation } from 'react-i18next'
import { Phone, MessageCircle, MapPin } from 'lucide-react'

export function Footer() {
  const { t } = useTranslation()
  const phone = import.meta.env.VITE_WHATSAPP_PHONE || '9535839987'

  return (
    <footer className="bg-krushi-green text-white py-12">
      <div className="container">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
          <div>
            <h3 className="font-bold text-lg mb-4">Sri Krushi Bhandara</h3>
            <p className="text-sm opacity-90">Smart agricultural solutions for better farming in Karnataka.</p>
          </div>

          <div>
            <h4 className="font-bold mb-4">Quick Links</h4>
            <ul className="space-y-2 text-sm">
              <li><a href="/" className="hover:text-krushi-yellow transition">Home</a></li>
              <li><a href="/products" className="hover:text-krushi-yellow transition">Products</a></li>
              <li><a href="/crop-doctor" className="hover:text-krushi-yellow transition">Crop Doctor</a></li>
              <li><a href="/contact" className="hover:text-krushi-yellow transition">Contact</a></li>
            </ul>
          </div>

          <div>
            <h4 className="font-bold mb-4">Categories</h4>
            <ul className="space-y-2 text-sm">
              <li><a href="#" className="hover:text-krushi-yellow transition">Fertilizers</a></li>
              <li><a href="#" className="hover:text-krushi-yellow transition">Crop Protection</a></li>
              <li><a href="#" className="hover:text-krushi-yellow transition">Micronutrients</a></li>
            </ul>
          </div>

          <div>
            <h4 className="font-bold mb-4">{t('footer.phone')}</h4>
            <div className="space-y-2 text-sm">
              <div className="flex items-center space-x-2">
                <Phone size={16} />
                <span>9535839987</span>
              </div>
              <div className="flex items-center space-x-2">
                <MessageCircle size={16} />
                <span>7483940895</span>
              </div>
              <div className="flex items-center space-x-2">
                <MapPin size={16} />
                <span className="text-xs">{t('footer.address')}</span>
              </div>
            </div>
          </div>
        </div>

        <div className="border-t border-opacity-20 pt-8 text-center text-sm">
          <p>{t('footer.copyright')}</p>
          <p className="mt-2 opacity-75">GSTIN: 29BYRPP6958A1ZQ</p>
        </div>
      </div>
    </footer>
  )
}
