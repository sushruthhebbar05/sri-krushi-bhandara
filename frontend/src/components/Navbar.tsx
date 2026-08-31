import React from 'react'
import { useTranslation } from 'react-i18next'
import { Globe } from 'lucide-react'

export function Navbar() {
  const { t, i18n } = useTranslation()
  const [menuOpen, setMenuOpen] = React.useState(false)

  const toggleLanguage = () => {
    const newLang = i18n.language === 'en' ? 'kn' : 'en'
    i18n.changeLanguage(newLang)
    localStorage.setItem('language', newLang)
  }

  return (
    <nav className="bg-white shadow-md sticky top-0 z-50">
      <div className="container flex items-center justify-between py-4">
        <div className="flex items-center space-x-2">
          <div className="w-10 h-10 bg-krushi-green rounded-full flex items-center justify-center text-white font-bold">
            ಕೃ
          </div>
          <span className="font-bold text-krushi-green text-lg hidden sm:inline">Sri Krushi Bhandara</span>
        </div>

        <div className="hidden md:flex items-center space-x-6">
          <a href="/" className="hover:text-krushi-yellow transition">{t('nav.home')}</a>
          <a href="/products" className="hover:text-krushi-yellow transition">{t('nav.products')}</a>
          <a href="/crop-doctor" className="hover:text-krushi-yellow transition">{t('nav.cropDoctor')}</a>
          <a href="/crops" className="hover:text-krushi-yellow transition">{t('nav.cropGuide')}</a>
          <a href="/about" className="hover:text-krushi-yellow transition">{t('nav.about')}</a>
          <a href="/contact" className="hover:text-krushi-yellow transition">{t('nav.contact')}</a>
        </div>

        <div className="flex items-center space-x-4">
          <button
            onClick={toggleLanguage}
            className="flex items-center space-x-1 text-krushi-green hover:text-krushi-yellow transition"
          >
            <Globe size={20} />
            <span className="text-sm font-medium">{i18n.language.toUpperCase()}</span>
          </button>
        </div>
      </div>
    </nav>
  )
}
