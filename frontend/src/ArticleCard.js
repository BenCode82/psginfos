import { Card, Col } from 'react-bootstrap';

const ArticleCard = ({ article }) => {
  return (
    <Col xs={12} sm={6} md={3} className="mb-4">
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
            <Card.Title>{article.titre}</Card.Title>
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
  );
};

export default ArticleCard;
