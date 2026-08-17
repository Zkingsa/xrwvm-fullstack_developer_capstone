import React, { useState } from 'react';

function Register() {
    const [formData, setFormData] = useState({
        username: '',
        firstName: '',
        lastName: '',
        email: '',
        password: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({ ...prev, [name]: value }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Registering:', formData);
        alert('Registration submitted!');
    };

    return (
        <div style={{ maxWidth: '400px', margin: '50px auto' }}>
            <h2>Sign Up</h2>
            <form onSubmit={handleSubmit}>
                <div style={{ marginBottom: '15px' }}>
                    <label>Username:</label><br />
                    <input type="text" name="username" value={formData.username} onChange={handleChange} required style={{ width: '100%' }} />
                </div>
                <div style={{ marginBottom: '15px' }}>
                    <label>First Name:</label><br />
                    <input type="text" name="firstName" value={formData.firstName} onChange={handleChange} required style={{ width: '100%' }} />
                </div>
                <div style={{ marginBottom: '15px' }}>
                    <label>Last Name:</label><br />
                    <input type="text" name="lastName" value={formData.lastName} onChange={handleChange} required style={{ width: '100%' }} />
                </div>
                <div style={{ marginBottom: '15px' }}>
                    <label>Email:</label><br />
                    <input type="email" name="email" value={formData.email} onChange={handleChange} required style={{ width: '100%' }} />
                </div>
                <div style={{ marginBottom: '15px' }}>
                    <label>Password:</label><br />
                    <input type="password" name="password" value={formData.password} onChange={handleChange} required style={{ width: '100%' }} />
                </div>
                <button type="submit" style={{ width: '100%', padding: '10px', background: '#007bff', color: '#fff', border: 'none' }}>Register</button>
            </form>
        </div>
    );
}

export default Register;
