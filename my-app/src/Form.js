import { useState } from 'react';
import reactLogo from "./face.png";
import reactLogo2 from "./dal.png";
 
export default function Form() {
 
  return (
    <div className="form">
      <div>
        <img className='dal' src={reactLogo2} alt="React Image" />
      </div>

      <br></br>

      <div>
        <h2>EDIT USER PROFILE</h2>
        <br></br>
        <h3>FirstName LastName</h3>
        <img src={reactLogo} alt="React Image" />
        <br></br>
        <button className='changePic'>Change Picture</button>
      </div>

      <br></br>

      <div>
        <h2>LinkedIn</h2>
        <input className="input" type="url" />
        <p className='eg'>eg:https://www.linkedin.com/feed/</p>
      </div>
      
      <br></br>

      <div>
        <h2>Contact</h2>
        <label className="label">Email</label>
        <input className="input" type="email" />
      </div>
      
      <br></br>

      <div>
        <h2>Personal Info</h2>
        <label className="label">Interest/Hobbies</label>
        <input className="input" type="text" />

        <label className="label">Future Goals</label>
        <input className="input" type="text" />

        <label className="label">Most Memorable Learning Experience</label>
        <input className="input" type="text" />
      </div>

      <br></br>
      <br></br>
      <br></br>
      <br></br>
      

      <div className="btn-group">
        <button className='save'>Save</button>
        <button className='delete'>Delete Account</button>
      </div>   

      <br></br> 
      <br></br> 
    </div>
  );
}