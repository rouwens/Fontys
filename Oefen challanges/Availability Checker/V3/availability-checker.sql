-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Gegenereerd op: 09 mrt 2021 om 13:22
-- Serverversie: 10.3.27-MariaDB-0+deb10u1-log
-- PHP-versie: 7.4.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `availability-checker`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `data`
--

CREATE TABLE `data` (
  `ID` int(255) NOT NULL,
  `gelukt` varchar(255) NOT NULL,
  `mislukt` varchar(255) NOT NULL,
  `url` text NOT NULL,
  `datum` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `test`
--

CREATE TABLE `test` (
  `ID` int(11) NOT NULL,
  `gelukt` int(255) DEFAULT NULL,
  `mislukt` int(255) DEFAULT NULL,
  `url` text DEFAULT NULL,
  `datum` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Gegevens worden geëxporteerd voor tabel `test`
--

INSERT INTO `test` (`ID`, `gelukt`, `mislukt`, `url`, `datum`) VALUES
(1, 1, 0, 'google.com', ''),
(2, 1, 0, 'google.com', ''),
(3, 1, 0, 'google.com', ''),
(4, 0, 1, 'facebook.com', ''),
(5, 0, 1, 'facebook.com', ''),
(9, 1, 0, 'google.com', ''),
(10, 0, 1, 'facebook.com', ''),
(11, 1, 0, 'facebook.com', ''),
(12, 1, 0, 'facebook.com', ''),
(13, 1, 0, 'youtube.com', ''),
(14, 1, 0, 'youtube.com', ''),
(15, 1, 0, 'youtube.com', ''),
(16, 1, 0, 'youtube.com', ''),
(17, 1, 0, 'youtube.com', ''),
(18, 1, 0, 'youtube.com', ''),
(19, 1, 0, 'youtube.com', ''),
(20, 1, 0, 'rouwens.ddns.net', '03/09/21'),
(21, 1, 0, 'rouwens.ddns.net', '03/09/21'),
(22, 1, 0, 'rouwens.ddns.net', '03/09/21'),
(23, 1, 0, 'rouwens.ddns.net', '03/09/21'),
(24, 1, 0, 'rouwens.ddns.net', '03/09/21'),
(25, 1, 0, 'rouwens.ddns.net', '03/09/21'),
(26, 1, 0, 'rouwens.ddns.net', '03/09/21'),
(27, 1, 0, 'rouwens.ddns.net', '03/09/21'),
(28, 0, 1, 'fontys.nl\\', '03/09/21'),
(29, 0, 1, 'fontys.nl', '03/09/21'),
(30, 0, 1, 'fontys.nl', '03/09/21'),
(31, 0, 1, 'fontys.nl', '03/09/21'),
(32, 0, 1, 'fontys.nl', '03/09/21'),
(33, 0, 1, 'fontys.nl', '03/09/21'),
(34, 0, 1, 'fontys.nl', '03/09/21'),
(35, 0, 1, 'fontys.nl', '03/09/21'),
(36, 0, 1, 'fontys.nl', '03/09/21'),
(37, 0, 1, 'fontys.nl', '03/09/21'),
(38, 0, 1, 'fontys.nl', '03/09/21'),
(39, 0, 1, 'fontys.nl', '03/09/21'),
(40, 0, 1, 'fontys.nl', '03/09/21'),
(41, 0, 1, 'fontys.nl', '03/09/21');

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `data`
--
ALTER TABLE `data`
  ADD PRIMARY KEY (`ID`);

--
-- Indexen voor tabel `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `data`
--
ALTER TABLE `data`
  MODIFY `ID` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT voor een tabel `test`
--
ALTER TABLE `test`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
