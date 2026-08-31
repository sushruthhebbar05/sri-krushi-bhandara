import React, { useState } from 'react'
import { useTranslation } from 'react-i18next'
import { useCropAnalysis } from '../hooks/useAPI'
import { Upload, Loader } from 'lucide-react'

export function CropDoctorHero() {
  const { t } = useTranslation()
  const [crop, setCrop] = useState('')
  const [symptoms, setSymptoms] = useState('')
  const [imageFile, setImageFile] = useState<File | null>(null)
  const [analysis, setAnalysis] = useState<any>(null)
  const { analyzeCrop, loading, error } = useCropAnalysis()

  const crops = [
    'Paddy',
    'Maize',
    'Arecanut',
    'Coffee',
    'Pepper',
    'Tomato',
    'Chilli',
    'Cotton',
    'Sugarcane',
    'Banana',
    'Coconut',
    'Vegetables',
  ]

  const handleAnalyze = async () => {
    if (!crop || !symptoms) {
      alert('Please select a crop and describe symptoms')
      return
    }
    const result = await analyzeCrop(crop, symptoms)
    setAnalysis(result)
  }

  return (
    <section className="bg-gradient-to-b from-krushi-green-light to-krushi-gray-bg py-16">
      <div className="container">
        <div className="max-w-2xl mx-auto">
          <h1 className="text-3xl md:text-4xl font-bold text-center mb-4 text-krushi-green">
            {t('cropDoctor.title')}
          </h1>
          <p className="text-center text-gray-600 mb-12">{t('cropDoctor.subtitle')}</p>

          <div className="bg-white rounded-lg shadow-lg p-8">
            {/* Step 1: Select Crop */}
            <div className="mb-6">
              <label className="block text-sm font-bold mb-2 text-krushi-dark">
                {t('cropDoctor.selectCrop')}
              </label>
              <select
                value={crop}
                onChange={(e) => setCrop(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-krushi-green"
              >
                <option value="">Select a crop...</option>
                {crops.map((c) => (
                  <option key={c} value={c}>
                    {c}
                  </option>
                ))}
              </select>
            </div>

            {/* Step 2: Upload Image */}
            <div className="mb-6">
              <label className="block text-sm font-bold mb-2 text-krushi-dark">
                {t('cropDoctor.uploadImage')}
              </label>
              <div className="border-2 border-dashed border-krushi-green rounded-lg p-8 text-center cursor-pointer hover:bg-krushi-gray-bg transition">
                <Upload className="mx-auto mb-2 text-krushi-green" size={32} />
                <input
                  type="file"
                  accept="image/*"
                  onChange={(e) => setImageFile(e.target.files?.[0] || null)}
                  className="hidden"
                  id="image-upload"
                />
                <label htmlFor="image-upload" className="cursor-pointer">
                  <p className="text-sm font-medium text-krushi-green">
                    {imageFile ? imageFile.name : 'Click to upload or drag and drop'}
                  </p>
                </label>
              </div>
            </div>

            {/* Step 3: Describe Symptoms */}
            <div className="mb-6">
              <label className="block text-sm font-bold mb-2 text-krushi-dark">
                {t('cropDoctor.describeSymptoms')}
              </label>
              <textarea
                value={symptoms}
                onChange={(e) => setSymptoms(e.target.value)}
                placeholder="Describe what you observe in the crop..."
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-krushi-green h-24"
              />
            </div>

            {/* Error Message */}
            {error && (
              <div className="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">
                {error}
              </div>
            )}

            {/* Analyze Button */}
            <button
              onClick={handleAnalyze}
              disabled={loading}
              className="w-full btn-primary flex items-center justify-center space-x-2 disabled:opacity-50"
            >
              {loading && <Loader size={20} className="animate-spin" />}
              <span>{t('cropDoctor.analyze')}</span>
            </button>
          </div>

          {/* Analysis Results */}
          {analysis && (
            <div className="mt-8 bg-white rounded-lg shadow-lg p-8">
              <h2 className="text-2xl font-bold mb-6 text-krushi-green">Analysis Result</h2>
              <div className="space-y-4">
                <div>
                  <h3 className="font-bold text-krushi-dark mb-2">Observations:</h3>
                  <ul className="list-disc list-inside space-y-1 text-gray-700">
                    {analysis.observations.map((obs: string, idx: number) => (
                      <li key={idx}>{obs}</li>
                    ))}
                  </ul>
                </div>

                {analysis.possible_issues.length > 0 && (
                  <div>
                    <h3 className="font-bold text-krushi-dark mb-2">Possible Issues:</h3>
                    <div className="space-y-2">
                      {analysis.possible_issues.map((issue: any, idx: number) => (
                        <div key={idx} className="p-3 bg-krushi-gray-bg rounded border-l-4 border-krushi-yellow">
                          <p className="font-bold text-krushi-dark">{issue.name}</p>
                          <p className="text-sm text-gray-600">{issue.description}</p>
                          <p className="text-xs text-gray-500 mt-1">
                            Confidence: {issue.confidence || analysis.confidence}
                          </p>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                <div>
                  <h3 className="font-bold text-krushi-dark mb-2">Recommended Next Steps:</h3>
                  <ol className="list-decimal list-inside space-y-1 text-gray-700">
                    {analysis.general_next_steps.map((step: string, idx: number) => (
                      <li key={idx}>{step}</li>
                    ))}
                  </ol>
                </div>

                <div className="p-4 bg-amber-50 border border-amber-200 rounded text-amber-900 text-sm">
                  <p className="font-bold mb-1">Safety Note:</p>
                  <p>{analysis.safety_note}</p>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </section>
  )
}
