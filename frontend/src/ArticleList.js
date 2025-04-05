import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Card, Container, Row, Col, Spinner } from 'react-bootstrap';

import './ArticleList.css';

function ArticleList() {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/articles/')
      .then(response => {
        const sorted = response.data.sort((a, b) => new Date(b.date_pub) - new Date(a.date_pub));
        setArticles(sorted);
        setLoading(false);
      })
      .catch(error => console.error("Erreur API :", error));
  }, []);

  return (
    <Container className="mt-5">
      {loading ? (
        <Spinner animation="border" />
      ) : (
        <Row>
          {articles.map(article => (
            <Col key={article.id} xs={12} sm={6} md={3} className="mb-4">
              <Card className="custom-card">
                <a href={article.lien} target="_blank" rel="noopener noreferrer" className="btn mt-2">

                  <Card.Img
                    variant="top"
                    src={article.image_url}
                    style={{
                      height: '200px',
                      objectFit: 'cover',
                      flex: '0 0 auto'
                    }}
                  />

                  <Card.Body style={{ flex: '1 1 auto' }}>
                    {<Card.Title>{article.titre}</Card.Title>}
                  </Card.Body>

                  <Card.Text>
                    {new Date(article.date_pub).toLocaleDateString('fr-FR', {
                      year: 'numeric',
                      month: 'long',
                      day: 'numeric',
                    })}
                    <br />
                    <small className="text-muted">{article.source}</small>
                  </Card.Text>

                </a>

              </Card>
            </Col>
          ))}
        </Row>
      )}
    </Container>
  );
}

export default ArticleList;
