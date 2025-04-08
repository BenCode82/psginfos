import React, { useState, useEffect } from 'react';
import { Container, Row,  Spinner } from 'react-bootstrap';
import axios from 'axios';

import './ArticleList.css';
import ArticleCard from './ArticleCard';

function ArticleList() {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // axios.get("https://benjaminmontet.alwaysdata.net/api/articles/")
    axios.get('http://127.0.0.1:8000/api/articles/')
      .then(response => {
        const sorted = response.data.sort((a, b) => new Date(b.date_pub) - new Date(a.date_pub));
        setArticles(sorted);
        setLoading(false);
      })
      .catch(error => console.error("Erreur API :", error));
  }, []);

  return (
    <>
      <div className="typewriter-container">
        <h1 className="typewriter-text typing-effect">
          Bienvenue sur le fil d'actus autour du PSG !
        </h1>
      </div>

      <Container className="mt-5">
        {loading ? (
          <Spinner animation="border" />
        ) : (
          <Row>
            {articles.map((article) => (
              <ArticleCard key={article.id} article={article} />
            ))}
          </Row>
        )}
      </Container>
    </>
  );
}

export default ArticleList;
