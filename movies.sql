-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 29, 2021 at 09:58 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mulesoft`
--

-- --------------------------------------------------------

--
-- Table structure for table `movies`
--

CREATE TABLE `movies` (
  `id` int(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `release_date` date NOT NULL,
  `director` varchar(50) NOT NULL,
  `lead_actor` varchar(50) NOT NULL,
  `lead_actress` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `movies`
--

INSERT INTO `movies` (`id`, `name`, `release_date`, `director`, `lead_actor`, `lead_actress`) VALUES
(1, 'Dune 2021', '2021-10-22', 'Denis Villeneuve', 'Timothée Chalamet', 'Zendaya'),
(2, 'Red Notice', '2021-11-05', 'Rawson Marshall Thurber', 'Dwayne Johnson, Ryan Reynolds', 'Gal Gadot'),
(4, 'Harry Potter and the Philosopher\'s Stone', '2002-04-12', ' Chris Columbus', 'Daniel Radcliffe', 'Emma Watson'),
(5, 'Spider-Man: Far from Home', '2019-07-02', 'Jon Watts', 'Tom Holland', 'Zendaya'),
(6, 'Shang-Chi and The Legend of The Ten Rings', '2021-09-02', 'Destin Daniel Cretton', 'Simu Liu', 'Awkwafina');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `movies`
--
ALTER TABLE `movies`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `movies`
--
ALTER TABLE `movies`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
