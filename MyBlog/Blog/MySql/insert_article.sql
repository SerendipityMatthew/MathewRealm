DROP TABLE if EXISTS article;
CREATE TABLE article (
    article_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (article_id),
    article_name VARCHAR(100) NOT NULL,
    article_author VARCHAR(20) NOT NULL,
    created_time DATE NOT NULL,
    article_tag VARCHAR(50) NOT NULL,
    reference_article VARCHAR(100) NOT NULL,
    reference_article_link VARCHAR(200) NOT NULL,
    related_article VARCHAR(200)
)ENGINE=InnoDB;

DROP TABLE IF EXISTS article_tag;
CREATE TABLE article_tag (
    tag_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (tag_id),
    tag_name VARCHAR(20) NOT NULL
)ENGINE=InnoDB;