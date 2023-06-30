-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 27, 2023 at 04:02 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kursus`
--

-- --------------------------------------------------------

--
-- Table structure for table `bimbel`
--

CREATE TABLE `bimbel` (
  `no` int(11) NOT NULL,
  `tgl_pendaftaran` date NOT NULL,
  `nama` varchar(250) NOT NULL,
  `alamat` varchar(245) NOT NULL,
  `telp` varchar(230) NOT NULL,
  `jeniskelamin` varchar(100) NOT NULL,
  `jeniskursus` varchar(235) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bimbel`
--

INSERT INTO `bimbel` (`no`, `tgl_pendaftaran`, `nama`, `alamat`, `telp`, `jeniskelamin`, `jeniskursus`) VALUES
(1, '2023-10-20', 'wisnu', 'kodam jayakarta', '08190242132444', 'Laki-Laki', 'Kursus Web Programming'),
(2, '2023-12-08', 'kazuhiro', 'osaka jepang', '081902421123242', 'Laki-Laki', 'Kursus Bahasa Java'),
(3, '2023-12-08', 'Khansa', 'limo Depok', '08190242423232', 'Perempuan', 'Kursus Python');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bimbel`
--
ALTER TABLE `bimbel`
  ADD PRIMARY KEY (`no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bimbel`
--
ALTER TABLE `bimbel`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
