import '../App.css'
import { useParallax } from 'react-scroll-parallax';

import CoolTrain from '../assets/CoolTrain.jpeg'

const Background = () => {
  const parallax = useParallax({ speed: 5 });

  return (
    <div ref={ parallax.ref }>
      <img  src={CoolTrain}
            alt="A cool train moving through some snow" 
            className="bg-image"
            style={{
              objectFit:"contain",
              boxShadow:"0 0 60px 20px var(--background-color) inset", 
              borderRadius:"8px",
              left:"25%",
              marginTop:"20%"
            }}
      />
    </div>
  );
}

export default Background;