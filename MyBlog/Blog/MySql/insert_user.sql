DROP TABLE IF EXISTS blog_user;
CREATE TABLE blog_user(
    user_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (user_id),
    username VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    phone_number VARCHAR(50)
)ENGINE=InnoDB;