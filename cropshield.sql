-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 06, 2025 at 09:36 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cropshield`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminlogin`
--

CREATE TABLE `adminlogin` (
  `AId` int(11) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `PhoneNo` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminlogin`
--

INSERT INTO `adminlogin` (`AId`, `Name`, `Password`, `Email`, `PhoneNo`) VALUES
(1, 'admin', '1234', 'admin@gmail.com', '7558569152'),
(2, 'Khushi Shewale', '8652', 'khushishewale797@gmail.com', '7558569152');

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `CId` int(11) NOT NULL,
  `CompanyName` varchar(70) NOT NULL,
  `Logo` text NOT NULL,
  `Email` varchar(70) NOT NULL,
  `PhoneNo` varchar(15) NOT NULL,
  `Address` text NOT NULL,
  `GSTno` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`CId`, `CompanyName`, `Logo`, `Email`, `PhoneNo`, `Address`, `GSTno`) VALUES
(1, 'AGRO SERVICES PVT. LTD.', 'logo.jpg', 'agroservices@wolfox.in', '9260089696', 'Sarudkar Building, 1767, E Ward, Near Yashwant Academy, Rajarampuri 3rd Lane, Kolhapur', '27AAACW1234Z1Z5');

-- --------------------------------------------------------

--
-- Table structure for table `cropcategory`
--

CREATE TABLE `cropcategory` (
  `CCId` int(11) NOT NULL,
  `Image` text NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cropcategory`
--

INSERT INTO `cropcategory` (`CCId`, `Image`, `Name`, `Description`) VALUES
(1, 'cropcat.jpg', 'Beverage Crops (पेय फसलें)', 'Crops used to produce drinks. Examples: tea, coffee'),
(2, 'cropcat.jpg', 'Grain Crops(अनाज फसल)', 'Crops like wheat, rice, maize, and millet grown for food and animal feed.'),
(3, 'cropcat.jpg', 'Fibre Crops (रेशेदार फसलें)', 'These crops are grown for textile and industrial use. Examples: cotton, jute, hemp.'),
(4, 'cropcat.jpg', 'Fruit Crops (फल वाली फसलें)', 'Vitamin-rich crops grown for direct consumption. Examples: mango, banana, papaya, coconut, orange.'),
(5, 'cropcat.jpg', 'Oilseed Crops (तेल वाली फसलें)', 'Crops used to extract edible and industrial oils. Examples include mustard, groundnut, soybean, and sunflower'),
(6, 'cropcat.jpg', 'Pulse Crops (दालें)', 'Protein-rich crops that form a vital part of the Indian diet. They also improve soil fertility. Examples: gram, pigeon pea (arhar), green gram (moong), black gram (urad), lentils.'),
(7, 'cropcat.jpg', 'Root_Tuber Crops (जड़ वाली फसलें)', 'Underground crops used for food and starch. Examples: potato, sweet potato, taro.'),
(8, 'cropcat.jpg', 'Spice Crops (मसाले)', 'Flavor-enhancing and medicinal crops. Examples: turmeric, ginger, coriander, black pepper, cardamom.'),
(9, 'cropcat.jpg', 'Sugar Crops (मीठी फसलें)', 'Crops that produce sugar and sweeteners. Examples: sugarcane, sugar beet.'),
(10, 'cropcat.jpg', 'Vegetable Crops (सब्जियाँ)', 'Nutritious crops consumed daily. Examples: tomato, cabbage, okra, brinjal, chili.'),
(11, 'cropcat.jpg', 'Forage Crops', 'Grown for feeding livestock. Examples: Napier grass, berseem, lucerne.');

-- --------------------------------------------------------

--
-- Table structure for table `crops`
--

CREATE TABLE `crops` (
  `CropId` int(11) NOT NULL,
  `CCId` int(11) NOT NULL COMMENT 'Crop Category Id\r\n',
  `Images` text NOT NULL,
  `CropName` varchar(50) NOT NULL,
  `Description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `crops`
--

INSERT INTO `crops` (`CropId`, `CCId`, `Images`, `CropName`, `Description`) VALUES
(1, 2, 'crop.jpg', 'Rice', 'A staple Kharif crop requiring high humidity and rainfall; rich in carbohydrates and widely consumed across India.'),
(2, 2, 'crop.jpg', 'Wheat', 'A Rabi crop grown in cooler climates; rich in protein and fiber, especially popular in northern India.'),
(3, 2, 'crop.jpg', 'Maize', 'Known as the \"queen of cereals\"; used for food, fodder, and industrial products like starch and oil.'),
(4, 6, 'crop.jpg', 'Gram (Chana)', 'A protein-rich Rabi pulse; drought-resistant and widely grown in central and western India.'),
(5, 6, 'crop.jpg', 'Pigeon Pea (Arhar)', 'A Kharif pulse used in dal; improves soil fertility through nitrogen fixation'),
(6, 6, 'crop.jpg', 'Green Gram (Moong)', 'A short-duration pulse crop; consumed as sprouts and dal, grown in summer and monsoon.'),
(7, 5, 'crop.jpg', 'Mustard', 'A Rabi oilseed crop; used for edible oil and condiments, grown in northern plains.'),
(8, 5, 'crop.jpg', 'Groundnut (Peanut)', 'A Kharif crop; used for oil extraction and snacks, thrives in sandy loam soil.'),
(9, 5, 'crop.jpg', 'Soybean', 'A high-protein oilseed; used in food, oil, and industrial products, grown in Madhya Pradesh and Maharashtra.'),
(10, 3, 'crop.jpg', 'Cotton', 'A Kharif crop; used in textiles, requires black soil and warm climate.'),
(11, 3, 'crop.jpg', 'Jute', 'A fibre crop grown in humid regions; used for making sacks, ropes, and carpets.'),
(12, 3, 'crop.jpg', 'Hemp (Sun)', 'A traditional fibre crop; used in ropes and coarse fabrics, grown in eastern India.'),
(13, 8, 'crop.jpg', 'Sugarcane', 'A major commercial crop; used for sugar, jaggery, and ethanol production.'),
(14, 9, 'crop.jpg', 'Sugar Beet', 'A temperate crop used for sugar extraction; less common but gaining popularity.'),
(15, 9, 'crop.jpg', 'Sweet Sorghum', 'Used for biofuel and syrup; drought-tolerant and grown in semi-arid regions.'),
(16, 7, 'crop.jpg', 'Potato', 'A Rabi crop; widely consumed, used in snacks and curries, grown in cool climates.'),
(17, 7, 'crop.jpg', 'Sweet Potato', 'A nutritious tuber; rich in fiber and vitamins, grown in sandy soil.'),
(18, 7, 'crop.jpg', 'Taro (Arbi)', 'A tropical root crop; used in traditional dishes, grown in moist conditions.'),
(19, 10, 'crop.jpg', 'Tomato', 'A widely grown vegetable; used in sauces, curries, and salads.'),
(20, 10, 'crop.jpg', 'Cabbage', 'A cool-season leafy vegetable; used in salads and stir-fries.'),
(21, 10, 'crop.jpg', 'Okra (Bhindi)', 'A warm-season crop; rich in fiber, used in Indian curries.'),
(22, 4, 'crop.jpg', 'Mango', 'The “king of fruits”; grown in summer, used fresh and in pickles.'),
(23, 4, 'crop.jpg', 'Banana', 'A year-round fruit; rich in potassium, used fresh and in snacks.'),
(24, 4, 'crop.jpg', 'Papaya', 'A tropical fruit; aids digestion, used fresh and in juices.'),
(25, 8, 'crop.jpg', 'Turmeric', 'A rhizome spice; used in cooking and Ayurveda, grown in moist climates.'),
(26, 8, 'crop.jpg', 'Ginger', 'A root spice; used in tea, curries, and medicine.'),
(27, 8, 'crop.jpg', 'Coriander', 'A dual-purpose crop; leaves used as garnish, seeds as spice.'),
(28, 1, 'crop.jpg', 'Tea', 'A perennial crop; grown in hilly regions, used for making black and green tea.'),
(29, 1, 'crop.jpg', 'Coffee', 'Grown in Karnataka and Kerala; used for beverages and export.'),
(30, 1, 'crop.jpg', 'Coffee', 'Grown in Karnataka and Kerala; used for beverages and export.'),
(31, 1, 'crop.jpg', 'Cocoa', 'Used for chocolate production; grown in tropical regions with shade.'),
(32, 12, 'crop.jpg', 'Napier Grass', 'A fast-growing fodder crop; used for dairy cattle.'),
(33, 12, 'crop.jpg', 'Berseem', 'A winter forage legume; high in protein, used for livestock.');

-- --------------------------------------------------------

--
-- Table structure for table `diseases`
--

CREATE TABLE `diseases` (
  `DId` int(11) NOT NULL,
  `CropId` int(11) NOT NULL COMMENT 'Crop Id',
  `PartId` int(11) NOT NULL COMMENT 'Crop Part Id',
  `Name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `diseases`
--

INSERT INTO `diseases` (`DId`, `CropId`, `PartId`, `Name`) VALUES
(1, 1, 1, 'Blast (Pyricularia oryzae)\n'),
(2, 1, 1, 'Brown Spot (Helminthosporium oryzae)\n'),
(3, 1, 1, 'Bacterial Leaf Blight (Xanthomonas oryzae)\n'),
(4, 1, 1, 'Leaf Streak (X. oryzae pv. oryzicola)'),
(5, 1, 1, 'Tungro Virus'),
(6, 1, 2, 'Sheath Blight (Rhizoctonia solani)\n'),
(7, 1, 2, 'Sheath Rot (Sarocladium oryzae)\n'),
(8, 1, 2, 'Stem Borer Damage\n'),
(9, 1, 3, 'False Smut (Ustilaginoidea virens)'),
(10, 1, 3, 'Grain Discoloration\n'),
(11, 1, 4, 'Root Rot (Pythium, Fusarium spp.)\n'),
(12, 1, 4, 'Root Knot Nematodes\n');

-- --------------------------------------------------------

--
-- Table structure for table `farmerlogin`
--

CREATE TABLE `farmerlogin` (
  `FId` int(11) NOT NULL,
  `Image` text NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `PhoneNo` varchar(15) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `Address` text NOT NULL,
  `Distric` varchar(20) NOT NULL,
  `State` varchar(20) NOT NULL,
  `Status` varchar(20) NOT NULL DEFAULT 'Active',
  `Date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `farmerlogin`
--

INSERT INTO `farmerlogin` (`FId`, `Image`, `Name`, `Email`, `PhoneNo`, `Password`, `Address`, `Distric`, `State`, `Status`, `Date`) VALUES
(1, 'user.jpg', 'Khushi Shewale', 'khushishewale797@gmail.com', '7558569152', '1234', 'Wategoan', 'Sangli', 'Maharashtra', 'Active', '2025-11-06 07:33:36'),
(2, 'user.jpg', 'Rajaram Shewale', 'rajaram@gmail.com', '7558569152', '8652', 'Wategoan Kasegoan', 'Sangli', 'Maharashtra', 'Active', '2025-10-14 14:02:28'),
(4, 'user.jpg', 'Sadhana', 'sadhna@gmail.com', '8766092044', '2222', 'Wategoan', 'Sangli', 'Maharashtra', 'Active', '2025-10-14 14:02:28'),
(5, 'user.jpg', 'shraddha thorat', 'shraddha@gmail.com', '9049236118', '1111', 'karad', 'satara', 'Maharashtra', 'Active', '2025-10-27 14:02:28'),
(6, 'user.jpg', 'Rutuja', 'rutujachavan710@gmail.com', '9373757906', '2222', 'Nvshari', 'Satara', 'Maharashtra', 'Active', '2025-11-06 05:49:28'),
(7, 'user.jpg', 'Shravani Bhosale', 'shravanibhosale195@gmail.com', '9307549847', '1111', 'Supane', 'Satara', 'Maharashtra', 'Active', '2025-11-06 05:51:17'),
(8, 'user.jpg', 'Dhanaji Thorat', 'shraddhadthorat2001@gmail.com', '7798710083', 'Sdt2001', 'karad', 'satara', 'maharastra', 'Active', '2025-11-01 05:12:13'),
(9, 'user.jpg', 'Fazal Inamdar', 'fazalinamdar.kst@gmail.com', '7798656165', '123456', 'C-22 Sanskruti City Malkapur', 'Satara', 'Maharashtra', 'Active', '2025-11-03 08:08:25');

-- --------------------------------------------------------

--
-- Table structure for table `farmerquery`
--

CREATE TABLE `farmerquery` (
  `FQId` int(11) NOT NULL,
  `FId` int(11) NOT NULL COMMENT 'Farmer Id',
  `FarmerName` varchar(50) NOT NULL,
  `CropName` varchar(50) NOT NULL COMMENT 'Store Crop Id',
  `PartName` varchar(50) NOT NULL COMMENT 'Store Crop Part Id',
  `SymptomsDetails` text NOT NULL,
  `SImg` text NOT NULL,
  `QueryStatus` varchar(15) NOT NULL DEFAULT 'Panding',
  `Date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `farmerquery`
--

INSERT INTO `farmerquery` (`FQId`, `FId`, `FarmerName`, `CropName`, `PartName`, `SymptomsDetails`, `SImg`, `QueryStatus`, `Date`) VALUES
(1, 1, 'Khushi Shewale', '1', '2', 'My wheat leaves are turning yellow from the tips and drying out.', 'fquery.jpg', 'Replied', '2025-11-06 07:34:53'),
(2, 5, 'Shraddha Thorat', '1', '1', 'What preventive measures can I take to protect crops?', 'fquery.jpg', 'Panding', '2025-11-06 07:16:10'),
(3, 5, 'Shraddha Thorat', '1', '3', 'Tomato fruits are getting black patches at the bottom and falling early.', 'fquery.jpg', 'Replied', '2025-11-06 07:36:33'),
(4, 1, 'Khushi Shewale', '1', '4', 'Rice plants are stunted and turning pale green. Growth is very slow.', 'fquery.jpg', 'Panding', '2025-11-06 07:21:48'),
(5, 8, 'Dhanaji Thorat', '1', '1', 'Leaves of my chili crop are curling and have tiny white insects.', 'fquery.jpg', 'Panding', '2025-11-06 07:50:06'),
(6, 1, 'Khushi Shewale', '1', '2', 'My maize crop has uneven growth and some plants are turning reddish.', 'fquery.jpg', 'Replied', '2025-11-06 07:51:13'),
(7, 9, 'Fazal Inamdar', '1', '2', 'Roots are quiet thick and crystal', 'fquery.jpg', 'Panding', '2025-11-06 07:16:33');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `Id` int(11) NOT NULL,
  `FId` int(11) NOT NULL COMMENT 'Farmer Id',
  `FeedBack` text NOT NULL,
  `Star` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`Id`, `FId`, `FeedBack`, `Star`) VALUES
(1, 1, 'The solar pump scheme you suggested saved my irrigation costs. Very helpful support!', 5),
(2, 3, 'Thanks to your guidance, my tomato crop recovered from disease. I’m now getting better yield!', 4),
(3, 6, 'I got a quick reply to my query about wheat pests. The solution worked perfectly.', 5),
(4, 1, 'Your platform makes it easy to ask questions in my own language. I feel confident using it.', 5),
(5, 7, 'The solar pump scheme info was very helpful. Just wish the reply came a bit faster.', 4),
(6, 4, 'The advice was good, but I had to ask twice before getting a response.', 3);

-- --------------------------------------------------------

--
-- Table structure for table `parts`
--

CREATE TABLE `parts` (
  `PartId` int(11) NOT NULL,
  `CrpId` int(11) NOT NULL COMMENT 'Crop Id',
  `Name` varchar(30) NOT NULL,
  `Image` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `parts`
--

INSERT INTO `parts` (`PartId`, `CrpId`, `Name`, `Image`) VALUES
(1, 1, 'Leaves ', 'cpart.jpg'),
(2, 1, 'Stem/Culm', 'cpart.jpg'),
(3, 1, 'Panicle & Grains ', 'cpart.jpg'),
(4, 1, 'Roots', 'cpart.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `PId` int(11) NOT NULL,
  `PCId` int(11) NOT NULL COMMENT 'Product Category Id',
  `DId` int(11) NOT NULL COMMENT 'Disease Id',
  `Name` varchar(60) NOT NULL,
  `Image` text NOT NULL,
  `Detail` text NOT NULL,
  `Usege` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`PId`, `PCId`, `DId`, `Name`, `Image`, `Detail`, `Usege`) VALUES
(1, 1, 1, 'Blast Off - Tricyclozole 75% WP', 'product.jpg', 'Being a quality centric organization, we are involved in manufacturing, exporting and supplying a quality range of BLAST OFF - Tricyclazole 75% WP in Amravati, Maharashtra, India.', 'BLAST OFF is Melanin biosynthesis inhibitor.  Systemic fungicide absorbed rapidly by the roots, with translocation through the plant.'),
(2, 1, 2, 'Indiagro Grow Magic', 'product.jpg', 'Indiagro Grow Magic Advance is a certified crop growth promoter for organic agriculture. It is a first-generation nanotech solution for overall crop development at significantly lesser doses per acre. This product has the right ingredients to strengthen and activate the plant’s natural defense system against bacteria, fungi, and viruses. It supplies powerful and nutrition growth stimulants. The product increases fruit texture, flavor, color, shape, odor fragrance, size, structure, pigmentation taste, palatability, and Reduces fruit and flower drops. You can buy Indiagro Grow Magic online in India from Big Value Shop at its best rate. The growth promoter is compatible with almost all liquid fertilizers and tank mixing chemicals. Grow magic improves photosynthesis and the plant’s ability to provide proteins, carbohydrates, and other essential growth elements. These essential compounds enhance root development and vegetative reproduction. Use sufficient amount of product for a better result. The ideal dose includes 100gm for 1 acre in 150/L of water. Indiagro Grow Magic cost is reasonable. Place your order now for more offers.', 'Use 5 days before: – Active vegetable growth stage Flowering stage Panicle initiation/ Active tillering/Fruit growth stages'),
(3, 1, 9, 'Indiagro Grow Magic Advance', 'product.jpg', 'Indiagro Grow Magic Advance is a certified crop growth promoter for organic agriculture. It is a first-generation nanotech solution for overall crop development at significantly lesser doses per acre. This product has the right ingredients to strengthen and activate the plant’s natural defense system against bacteria, fungi, and viruses. It supplies powerful and nutrition growth stimulants.', 'Use 5 days before: – Active vegetable growth stage Flowering stage Panicle initiation/ Active tillering/Fruit growth stages'),
(4, 2, 3, 'PetraGrow Leaf Guard', 'product.jpg', 'PetraGrow Leaf Guard is a ready-to-use liquid formulation designed to protect crops from a wide range of pests and diseases. It functions as a pesticide, fungicide, and miticide, making it suitable for rice crops affected by leaf blast, brown spot, powdery mildew, and sap-sucking insects. The product is safe for edible plants and can be used both indoors and outdoors.', 'To use PetraGrow Leaf Guard, the bottle should be shaken well before application to ensure the ingredients are evenly mixed. The spray is applied directly to the leaves, stems, and affected areas using a hand sprayer or backpack sprayer. Its important to coat the surface evenly without causing runoff. For best results, spraying should be done during early morning or late afternoon, avoiding strong sunlight or rain. During active infestation or disease outbreaks, the spray should be applied every 7 to 10 days. For preventive care, it can be used once every two to three weeks.'),
(5, 2, 4, 'PetraGrow Leaf Guard', 'product.jpg', 'PetraGrow Leaf Guard is a ready-to-use liquid formulation designed to protect crops from a wide range of pests and diseases. It functions as a pesticide, fungicide, and miticide, making it suitable for rice crops affected by leaf blast, brown spot, powdery mildew, and sap-sucking insects. The product is safe for edible plants and can be used both indoors and outdoors.', 'To use PetraGrow Leaf Guard, the bottle should be shaken well before application to ensure the ingredients are evenly mixed. The spray is applied directly to the leaves, stems, and affected areas using a hand sprayer or backpack sprayer. '),
(6, 3, 5, 'Organic antiviral sprays or neem-based formulations (custom ', 'product.jpg', 'Organic antiviral sprays and neem-based formulations are used to suppress viral infections in rice crops like Tungro virus. These products are typically made from botanical extracts such as neem oil, pongamia, or seaweed, and are safe for edible crops.', 'They work by boosting the plant’s natural immunity and creating a protective barrier against viral vectors like leafhoppers. To use, dilute 3–5 ml of the product per liter of water and apply as a foliar spray during early morning or late evening. Begin spraying at the first sign of viral symptoms and repeat every 7–10 days for effective control'),
(7, 1, 6, 'Beam Fungicide', 'product.png', 'beam of timber ®. It contains the active ingredient, tricyclazole, which is related to melanin biosynthesis inhibitors. The beam provides the best control of the explosion at all stages of development. It has prophylactic action. Highly systemic-good leaf and root capture with xylem motility No resistance issues have been registered to date.', 'Tricyclazole inhibits the polyhydroxynaphthalin reductase enzyme and thus inhibits the formation of melanin in fungi (Pyricularia griacea). In the absence of melanin, the apresoria fails to produce the penetrating hyphae or the penetrating hyphae fails to enter the host tissue. Therefore, the disease is not allowed to spread. This does not allow the fungus to establish by preventing it from entering the plant system. It is highly systemic in action, thus it is rapidly absorbed by the leaves and roots of the rice and transferred towards the tip of the leaf, suggesting its xylem transport. There is also movement from a treated foliage to untreated young leaves.'),
(8, 1, 7, 'Blast Off - Tricyclozole', 'product.jpg', 'Being a quality centric organization, we are involved in manufacturing, exporting and supplying a quality range of BLAST OFF - Tricyclazole 75% WP in Amravati, Maharashtra, India.', 'BLAST OFF is Melanin biosynthesis inhibitor. Systemic fungicide absorbed rapidly by the roots, with translocation through the plant.'),
(9, 6, 8, 'Bayer Advanced Insect Spray', 'product.jpg', 'Kills over 70 listed insects including Aphids, Caterpillars, Thrips, Tomato Hornworm, and Whiteflies Protects fruits and vegetables from insect damage, for outdoor use Easy application by spraying onto plant until leaves are evenly coated, but not dripping Rainproof protection in just 1 hour Coverage area treats up to 5,333 square feet Contains 0.75% Cyfluthrin as active ingredient with EPA Registration Number: 92564-17', 'BioAdvanced Vegetable and Garden Insect Spray helps protect your garden from listed pests damage. This insecticide concentrate is helpful in targeting and killing aphids, caterpillars, thrips, tomato hornworms, whiteflies and over 70 other listed insects. The formulation is designed for outdoor use, providing protection for your fruits and vegetables against harmful listed insects. Application is straightforward: mix the concentrate with water and just spray onto your plants until the leaves are uniformly coated but not dripping. With its rainproof protection, this insect killer is rain-resistant in just one hour. BioAdvanced Vegetable & Garden Insect Killer not only protects your produce but also extends its protective reach to lawns, flowers, shrubs, and trees, making it helpful for various garden needs. The 32-ounce concentrate treats up to 5,333 square feet of lawn and yields up to 64 gallons of spray. Active Ingredients: 0.75% Cyfluthrin EPA Registration Number: 92564-17'),
(10, 4, 10, 'Combo packs with zinc, copper, and fungicide blends', 'product.jpg', 'Combo packs containing zinc, copper, and fungicide blends are designed to improve rice crop health by controlling fungal infections and correcting micronutrient deficiencies. These packs typically include a systemic fungicide like Tricyclozole or Mancozeb, combined with zinc sulfate and copper oxychloride.', 'They are used as foliar sprays during the panicle initiation and grain filling stages. Mix 500 ml to 1 liter of the combo solution per acre in 150–200 liters of water. Spray uniformly over the crop canopy during early morning or late evening. Repeat every 10–12 days if symptoms persist, especially for diseases like grain discoloration, sheath rot, and leaf blast.'),
(11, 5, 11, 'Trichoderma-based biofungicides', 'product.jpg', 'These are organic fungal biocontrol agents made from Trichoderma harzianum or Trichoderma viride. They suppress soil-borne pathogens like Pythium, Fusarium, and Rhizoctonia, which cause root rot and damping-off in rice and other crops. Available in powder or liquid form, they are eco-friendly and promote root health.', '- Soil Application: Mix 2–3 kg of powder or 1 liter of liquid in 50 kg of compost or FYM (farmyard manure) and broadcast over 1 acre before transplanting. - Root Dip: For seedlings, prepare a slurry (5 g/L water) and dip roots for 30 minutes before transplanting. - Drip/Foliar Spray: Use 5 ml/L water for foliar spray or 1 liter/acre via drip irrigation.'),
(12, 9, 12, 'Nematode Detection', 'product.jpg', 'These kits are designed for integrated nematode management. They typically include a nematode detection strip or soil test kit, neem cake (natural nematicide), and biofertilizers like Pseudomonas fluorescens or Azotobacter to restore soil health.', '- Detection: Use the soil test strip or kit to check for nematode presence before sowing. - Neem Cake Application: Apply 100–200 kg per acre during land preparation. Mix well into the soil 10–15 days before transplanting. - Biofertilizer Application: Mix 2–4 kg of biofertilizer with compost and apply near the root zone or use as a seedling dip before transplanting.'),
(13, 10, 12, 'Biofertilizer Kits', 'product.jpg', 'These kits are designed for integrated nematode management. They typically include a nematode detection strip or soil test kit, neem cake (natural nematicide), and biofertilizers like Pseudomonas fluorescens or Azotobacter to restore soil health.', '- Detection: Use the soil test strip or kit to check for nematode presence before sowing. - Neem Cake Application: Apply 100–200 kg per acre during land preparation. Mix well into the soil 10–15 days before transplanting. - Biofertilizer Application: Mix 2–4 kg of biofertilizer with compost and apply near the root zone or use as a seedling dip before transplanting.');

-- --------------------------------------------------------

--
-- Table structure for table `productcategory`
--

CREATE TABLE `productcategory` (
  `PCId` int(11) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Image` text NOT NULL,
  `Description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `productcategory`
--

INSERT INTO `productcategory` (`PCId`, `Name`, `Image`, `Description`) VALUES
(1, 'Fungicides', 'procat.jpg', 'Products to control fungal infections in crops'),
(2, 'Bactericides', 'procat.jpg', 'Solutions for bacterial diseases affecting plants'),
(3, 'Viral Suppressants', 'procat.jpg', 'Treatments to reduce viral impact on crops'),
(4, 'Micronutrient Mixes', 'procat.jpg', 'Boost crop health with essential nutrients'),
(5, 'Biofertilizers', 'procat.jpg', 'Organic fertilizers that improve soil fertility'),
(6, 'Pest Traps', 'procat.jpg', 'Tools to capture and monitor crop pests'),
(7, 'Protective Netting', 'procat.jpg', 'Mesh and covers to shield crops from insects'),
(8, 'Root Stimulants', 'procat.jpg', 'Enhance root development and nutrient uptake'),
(9, 'Soil Testing Kits', 'procat.jpg', 'DIY kits to analyze soil health and composition'),
(10, 'Treatment Combo Packs', 'procat.jpg', 'Ready-to-use bundles for crop-specific protection');

-- --------------------------------------------------------

--
-- Table structure for table `replayquery`
--

CREATE TABLE `replayquery` (
  `RQId` int(11) NOT NULL,
  `FQId` int(11) NOT NULL COMMENT 'Farmer Query Id',
  `Question` text NOT NULL,
  `Answer` text NOT NULL,
  `Position` varchar(25) NOT NULL DEFAULT 'Private',
  `SuggestProduct` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `replayquery`
--

INSERT INTO `replayquery` (`RQId`, `FQId`, `Question`, `Answer`, `Position`, `SuggestProduct`) VALUES
(1, 1, 'Is the yellowing starting from older leaves or new ones? Have you applied any fertilizer recently?', 'This looks like nitrogen deficiency. Apply Urea @ 45kg/acre and ensure proper irrigation.', 'Private', '3'),
(2, 3, 'Are the leaves healthy? Is watering consistent or irregular?', 'This is Blossom End Rot due to calcium deficiency. Use calcium nitrate foliar spray and maintain regular watering.', 'public', '6'),
(3, 5, 'Are the insects visible on the underside of leaves? Do you see sticky residue?', 'This is whitefly infestation. Spray Imidacloprid 17.8% SL @ 0.5ml/litre and repeat after 7 days.', 'public', '2'),
(6, 6, 'Is the reddish color on lower leaves? Have you tested soil nutrients?', 'This may be potassium deficiency. Apply MOP @ 40kg/acre and monitor soil pH.', 'Private', '11');

-- --------------------------------------------------------

--
-- Table structure for table `symptoms`
--

CREATE TABLE `symptoms` (
  `SId` int(11) NOT NULL,
  `DId` int(11) NOT NULL COMMENT 'Disease Id',
  `Image` text NOT NULL,
  `Description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `symptoms`
--

INSERT INTO `symptoms` (`SId`, `DId`, `Image`, `Description`) VALUES
(1, 1, 'symptoms.jpg', 'Grayish lesions with brown margins, often diamond-shaped. Starts from leaf tips and spreads rapidly. - '),
(2, 2, 'symptoms.jpg', 'Small, round or oval brown spots, sesame-sized. Appears from seedling to grain stage.'),
(3, 3, 'symptoms.jpg', 'Yellowing from leaf tip downward, wilting in severe cases. Common in humid conditions.'),
(4, 4, 'symptoms.jpg', 'Narrow, water-soaked streaks that turn yellow. Often confused with blight.'),
(5, 5, 'symptoms.jpg', 'Orange-yellow leaf discoloration, stunted growth, poor panicle development.'),
(6, 6, 'symptoms.jpg', 'Irregular greenish-gray lesions on leaf sheath, spreading to stem. Favored by dense planting.'),
(7, 7, 'symptoms.jpg', 'Brown discoloration and rotting of leaf sheath near panicle base. Affects grain formation.'),
(8, 8, 'symptoms.jpg', 'Dead heart in young plants, whiteheads in mature ones. Caused by larvae boring into stem.'),
(9, 9, 'symptoms.jpg', 'Yellow-green fungal balls replace grains. Reduces grain quality.'),
(10, 10, 'symptoms.jpg', 'Black, brown, or reddish patches due to fungal complex. Affects market value.'),
(11, 11, 'symptoms.jpg', 'Blackened, decayed roots, poor tillering. Often due to waterlogging.'),
(12, 12, 'symptoms.jpg', 'Swollen root tips, stunted growth. Reduces nutrient uptake.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminlogin`
--
ALTER TABLE `adminlogin`
  ADD PRIMARY KEY (`AId`);

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`CId`);

--
-- Indexes for table `cropcategory`
--
ALTER TABLE `cropcategory`
  ADD PRIMARY KEY (`CCId`);

--
-- Indexes for table `crops`
--
ALTER TABLE `crops`
  ADD PRIMARY KEY (`CropId`);

--
-- Indexes for table `diseases`
--
ALTER TABLE `diseases`
  ADD PRIMARY KEY (`DId`);

--
-- Indexes for table `farmerlogin`
--
ALTER TABLE `farmerlogin`
  ADD PRIMARY KEY (`FId`);

--
-- Indexes for table `farmerquery`
--
ALTER TABLE `farmerquery`
  ADD PRIMARY KEY (`FQId`);

--
-- Indexes for table `parts`
--
ALTER TABLE `parts`
  ADD PRIMARY KEY (`PartId`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`PId`);

--
-- Indexes for table `productcategory`
--
ALTER TABLE `productcategory`
  ADD PRIMARY KEY (`PCId`);

--
-- Indexes for table `replayquery`
--
ALTER TABLE `replayquery`
  ADD PRIMARY KEY (`RQId`);

--
-- Indexes for table `symptoms`
--
ALTER TABLE `symptoms`
  ADD PRIMARY KEY (`SId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adminlogin`
--
ALTER TABLE `adminlogin`
  MODIFY `AId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `company`
--
ALTER TABLE `company`
  MODIFY `CId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `cropcategory`
--
ALTER TABLE `cropcategory`
  MODIFY `CCId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `crops`
--
ALTER TABLE `crops`
  MODIFY `CropId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `diseases`
--
ALTER TABLE `diseases`
  MODIFY `DId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `farmerlogin`
--
ALTER TABLE `farmerlogin`
  MODIFY `FId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `farmerquery`
--
ALTER TABLE `farmerquery`
  MODIFY `FQId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `parts`
--
ALTER TABLE `parts`
  MODIFY `PartId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `PId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `productcategory`
--
ALTER TABLE `productcategory`
  MODIFY `PCId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `replayquery`
--
ALTER TABLE `replayquery`
  MODIFY `RQId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `symptoms`
--
ALTER TABLE `symptoms`
  MODIFY `SId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
