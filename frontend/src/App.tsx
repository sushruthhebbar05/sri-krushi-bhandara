import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './i18n'
import { Navbar } from './components/Navbar'
import { Footer } from './components/Footer'
import { Hero } from './components/Hero'
import { FeaturedProducts } from './components/FeaturedProducts'
import { CropDoctorHero } from './components/CropDoctorHero'

function HomePage() {
  return (
    <>
      <Hero />
      <FeaturedProducts />
      <section className="py-16 bg-krushi-green text-white text-center">
        <div className="container">
          <h2 className="text-3xl font-bold mb-6">Smart Agricultural Solutions for Better Farming</h2>
          <p className="text-lg mb-8 max-w-2xl mx-auto opacity-90">
            From fertilizers and crop protection to AI-assisted crop guidance, Sri Krushi Bhandara helps farmers make smarter agricultural decisions.
          </p>
          <a href="/contact" className="inline-block bg-krushi-yellow text-krushi-green font-bold px-8 py-3 rounded-lg hover:bg-white transition">
            Get Started Today
          </a>
        </div>
      </section>
    </>
  )
}

function CropDoctorPage() {
  return <CropDoctorHero />
}

function App() {
  return (
    <Router>
      <div className="min-h-screen flex flex-col">
        <Navbar />
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/crop-doctor" element={<CropDoctorPage />} />
            <Route path="/products" element={<div className="container py-16"><h1 className="text-3xl font-bold">Products Coming Soon</h1></div>} />
            <Route path="/crops" element={<div className="container py-16"><h1 className="text-3xl font-bold">Crop Guide Coming Soon</h1></div>} />
            <Route path="/about" element={<div className="container py-16"><h1 className="text-3xl font-bold">About Us Coming Soon</h1></div>} />
            <Route path="/contact" element={<div className="container py-16"><h1 className="text-3xl font-bold">Contact Coming Soon</h1></div>} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  )
}

export default App
