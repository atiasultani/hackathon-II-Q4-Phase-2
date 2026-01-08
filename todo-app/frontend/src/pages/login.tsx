import React, { useState } from 'react';
import LoginForm from '../components/LoginForm';
import RegisterForm from '../components/RegisterForm';

const LoginPage: React.FC = () => {
  const [showRegister, setShowRegister] = useState(false);

  return (
    <div className="min-h-screen flex">
      {showRegister ? (
        <RegisterForm
          switchToLogin={() => setShowRegister(false)}
        />
      ) : (
        <LoginForm
          switchToRegister={() => setShowRegister(true)}
        />
      )}
    </div>
  );
};

export default LoginPage;