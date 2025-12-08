import React, { useState } from 'react';
import styles from './styles.module.css';

interface PersonalizationButtonProps {
  chapterId: number;
  onPersonalize?: (settings: PersonalizationSettings) => void;
}

interface PersonalizationSettings {
  experienceLevel: 'beginner' | 'intermediate' | 'advanced';
  learningGoal: 'academic' | 'career' | 'hobby' | 'research';
  preferredDepth: 'overview' | 'detailed' | 'research';
  domainInterests: string[];
}

const PersonalizationButton: React.FC<PersonalizationButtonProps> = ({
  chapterId,
  onPersonalize,
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [settings, setSettings] = useState<PersonalizationSettings>({
    experienceLevel: 'beginner',
    learningGoal: 'academic',
    preferredDepth: 'overview',
    domainInterests: [],
  });

  const handlePersonalize = async () => {
    setIsLoading(true);
    try {
      // TODO: Call personalization API
      // const response = await fetch(`/api/personalize/chapter/${chapterId}`, {
      //   method: 'POST',
      //   headers: { 'Content-Type': 'application/json' },
      //   body: JSON.stringify(settings),
      // });
      
      // For now, just call the callback
      if (onPersonalize) {
        onPersonalize(settings);
      }
      
      // Show success message
      alert('Content personalized successfully!');
      setIsOpen(false);
    } catch (error) {
      console.error('Personalization error:', error);
      alert('Failed to personalize content. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  const toggleInterest = (interest: string) => {
    setSettings((prev) => ({
      ...prev,
      domainInterests: prev.domainInterests.includes(interest)
        ? prev.domainInterests.filter((i) => i !== interest)
        : [...prev.domainInterests, interest],
    }));
  };

  return (
    <div className={styles.personalizationContainer}>
      <button
        className={styles.personalizeButton}
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Personalize Content"
      >
        🎯 Personalize This Chapter
      </button>

      {isOpen && (
        <div className={styles.modal}>
          <div className={styles.modalContent}>
            <h3>Personalize Your Learning Experience</h3>
            <p>Customize this chapter based on your background and goals.</p>

            <div className={styles.formGroup}>
              <label>Experience Level</label>
              <select
                value={settings.experienceLevel}
                onChange={(e) =>
                  setSettings({
                    ...settings,
                    experienceLevel: e.target.value as PersonalizationSettings['experienceLevel'],
                  })
                }
              >
                <option value="beginner">Beginner</option>
                <option value="intermediate">Intermediate</option>
                <option value="advanced">Advanced</option>
              </select>
            </div>

            <div className={styles.formGroup}>
              <label>Learning Goal</label>
              <select
                value={settings.learningGoal}
                onChange={(e) =>
                  setSettings({
                    ...settings,
                    learningGoal: e.target.value as PersonalizationSettings['learningGoal'],
                  })
                }
              >
                <option value="academic">Academic</option>
                <option value="career">Career Transition</option>
                <option value="hobby">Hobby/Interest</option>
                <option value="research">Research</option>
              </select>
            </div>

            <div className={styles.formGroup}>
              <label>Preferred Depth</label>
              <select
                value={settings.preferredDepth}
                onChange={(e) =>
                  setSettings({
                    ...settings,
                    preferredDepth: e.target.value as PersonalizationSettings['preferredDepth'],
                  })
                }
              >
                <option value="overview">High-Level Overview</option>
                <option value="detailed">Detailed Technical</option>
                <option value="research">Research-Level</option>
              </select>
            </div>

            <div className={styles.formGroup}>
              <label>Domain Interests</label>
              <div className={styles.checkboxGroup}>
                {['Hardware', 'Software', 'AI Algorithms', 'Applications', 'Robotics', 'Simulation'].map(
                  (interest) => (
                    <label key={interest} className={styles.checkboxLabel}>
                      <input
                        type="checkbox"
                        checked={settings.domainInterests.includes(interest)}
                        onChange={() => toggleInterest(interest)}
                      />
                      {interest}
                    </label>
                  )
                )}
              </div>
            </div>

            <div className={styles.buttonGroup}>
              <button
                className={styles.cancelButton}
                onClick={() => setIsOpen(false)}
              >
                Cancel
              </button>
              <button
                className={styles.applyButton}
                onClick={handlePersonalize}
                disabled={isLoading}
              >
                {isLoading ? 'Applying...' : 'Apply Personalization'}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default PersonalizationButton;

