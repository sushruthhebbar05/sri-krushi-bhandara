import React from 'react'
import { useTranslation } from 'react-i18next'

export function Hero() {
  const { t } = useTranslation()

  return (
    <section className="bg-gradient-to-r from-krushi-green to-krushi-green-light text-white py-20">
      <div className="container text-center">
        <h1 className="text-4xl md:text-5xl font-bold mb-6">{t('hero.headline')}</h1>
        <p className="text-lg md:text-xl mb-8 max-w-2xl mx-auto opacity-90">
          {t('hero.subheadline')}
        </p>
        <div className="flex flex-col md:flex-row gap-4 justify-center">
          <a href="/products" className="btn-primary">
            {t('hero.ctaPrimary')}
          </a>
          <a href="/crop-doctor" className="btn-secondary text-white border-white hover:bg-white hover:text-krushi-green">
            {t('hero.ctaSecondary')}
          </a>
          <a href="/contact" className="btn-secondary text-white border-white hover:bg-white hover:text-krushi-green">
            {t('hero.ctaTertiary')}
          </a>
        </div>
      </div>
    </section>
  )
}
