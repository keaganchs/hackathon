import React from "react"
import { useParallax } from 'react-scroll-parallax';

const Info = () => {
  const parallax = useParallax({ speed: 5 });

  return (
    <div className="InfoContainer">
      <div className="SubtitleContainer" ref={parallax.ref}>
        <h2>
          <i>Training Future Generations.</i>
        </h2>
      </div>

      <p>
        Carbon Trainer. We show the potential carbon savings of high occupancy transportation, in hopes to improve global sustainability.
      </p>

    </div>
  )
}

export default Info;