import React, { useState, useEffect } from 'react';
import { Container, Row,  Spinner } from 'react-bootstrap';
import axios from 'axios';

import AOS from 'aos';
import 'aos/dist/aos.css';

import './ArticleList.css';
import ArticleCard from './ArticleCard';

function ArticleList() {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => { // Fetch sur l'API
    axios.get("https://benjaminmontet.alwaysdata.net/api/articles/")
    // axios.get('http://127.0.0.1:8000/api/articles/')
      .then(response => {
        const sorted = response.data.sort((a, b) => new Date(b.date_pub) - new Date(a.date_pub));
        setArticles(sorted);
        setLoading(false);

      })
    .catch(error => console.error("Erreur API :", error));
  }, []);

  useEffect(() => { // AOS : animer des éléments sur le scroll
    AOS.init({
      duration: 800,       // Durée animation (ms)
      easing: 'ease-in-out', // Type d'animation
      once: true,
      mirror: false,       // Ne pas re-animer en remontant
      offset: 200,         // Déclenchement 120px avant l'élément
    });
  }, []);

  useEffect(() => { // progress bar en bas de page
    const handleScroll = () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const scrollPercent = (scrollTop / docHeight) * 100;
      const progressBar = document.getElementById("progress-bar");
      if (progressBar) {
        progressBar.style.width = `${scrollPercent}%`;
      }
    };

  }, []);

  return (
    <>

      <div data-aos="fade-up">
        <main>
          <header className="typewriter-container">
            <h1 className="typewriter-text typing-effect">
              Bienvenue sur le fil d'actus autour du PSG !
            </h1>
          </header>

          <Container className="mt-5">
            {loading ? (
              <Spinner animation="border" />
            ) : (
              <Row>
                {articles.map((article) => (
                  <ArticleCard article={article}/>
                ))}
              </Row>
            )}
          </Container>
        </main>

        <footer className="footer">
          <p>© {new Date().getFullYear()} - Propulsé par React ⚛️ & Django 🐍</p>
        </footer>
      </div>

      <div id="progress-bar"></div>

    </>
  );
}

export default ArticleList;
