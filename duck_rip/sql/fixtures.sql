USE `duck_finance`;

INSERT INTO `sf_guard_user` (`id`, `first_name`, `last_name`, `email_address`, `username`, `algorithm`, `salt`, `password`, `is_active`, `is_super_admin`, `last_login`, `created_at`, `updated_at`) VALUES
(1, 'Paul', 'McCartney', 'paul.mccartney@beatles.com', 'pmc', 'sha1', '9137e482c18a1a9bb34ef7b992c79929', '2085e867458db5de8660402a0f50a8cf7d446235', 1, 1, '2011-10-18 19:22:27', '2011-10-18 19:22:27', '2011-10-18 19:22:27'),
(2, 'John', 'Lennon', 'john.lennon@beatles.com', 'jl', 'sha1', '023b9c69a98e8bd0fa0960cf61ceb015', '8302ab7ba2febf30101dca94f046116652292f78', 1, 1, '2011-10-18 19:22:27', '2011-10-18 19:22:27', '2011-10-18 19:22:27'),
(3, 'George', 'Harrison', 'george.harrison@beatles.com', 'gh', 'sha1', 'c69a961908e8bd0f960ceb015a03bcf2', '8302ab7ba2febf30101dca94f046116652292f78', 1, 1, '2011-10-18 19:22:27', '2011-10-18 19:22:27', '2011-10-18 19:22:27'),
(4, 'Ringo', 'Starr', 'ringo.starr@beatles.com', 'rs', 'sha1', 'aa0fb90823158bde961ceb0960cf0c69', '8302ab7ba2febf30101dca94f046116652292f78', 1, 1, '2011-10-18 19:22:27', '2011-10-18 19:22:27', '2011-10-18 19:22:27');

INSERT INTO `category` (`id`, `parent_id`, `name`, `type`, `created_at`, `updated_at`, `created_by`, `updated_by`) VALUES
(1, NULL, 'food', 'Outcome', '2011-10-18 19:22:27', '2011-10-18 19:22:27', 2, 2),
(2, NULL, 'bills', 'Outcome', '2011-10-18 19:22:27', '2011-10-18 19:22:27', 2, 2),
(3, NULL, 'electronics', 'Outcome', '2011-10-18 19:22:27', '2011-10-18 19:22:27', 2, 2),
(4, NULL, 'entertainment', 'Outcome', '2011-10-18 19:22:27', '2011-10-18 19:22:27', 2, 2),
(10, NULL, 'transport', 'Outcome', '2011-10-20 19:57:12', '2011-10-20 19:57:12', 2, 2),
(12, NULL, 'books', 'Outcome', '2011-10-20 20:08:46', '2011-10-20 20:08:46', 2, 2),
(14, NULL, 'hygiene', 'Outcome', '2011-10-20 20:11:38', '2011-10-20 20:11:38', 2, 2),
(16, NULL, 'house', 'Outcome', '2011-10-20 20:17:47', '2011-10-20 20:17:47', 2, 2),
(20, NULL, 'presents', 'Outcome', '2011-10-20 20:42:31', '2011-10-20 20:42:31', 2, 2),
(23, NULL, 'footwear', 'Outcome', '2011-10-20 23:15:21', '2011-10-20 23:15:21', 2, 2),
(24, NULL, 'clothing', 'Outcome', '2011-10-20 23:15:25', '2011-10-20 23:15:25', 2, 2),
(34, NULL, 'education', 'Outcome', '2011-10-29 21:24:52', '2011-10-29 21:24:52', 2, 2),
(49, NULL, 'health', 'Outcome', '2012-03-23 10:48:39', '2012-03-23 10:48:39', 2, 2),
(5, 4, 'travels', 'Outcome', '2011-10-18 19:22:27', '2011-10-20 20:52:21', 2, 2),
(6, 1, 'bread', 'Outcome', '2011-10-20 19:05:00', '2011-10-20 19:05:00', 2, 2),
(7, 4, 'bar', 'Outcome', '2011-10-20 19:20:08', '2011-10-20 19:20:08', 2, 2),
(8, 1, 'fruits & vegs', 'Outcome', '2011-10-20 19:20:17', '2011-10-22 05:36:49', 2, 2),
(9, 4, 'press', 'Outcome', '2011-10-20 19:56:56', '2011-10-20 20:52:04', 2, 2),
(11, 1, 'lunch', 'Outcome', '2011-10-20 19:57:34', '2011-10-20 19:57:48', 2, 2),
(13, 16, 'chemistry', 'Outcome', '2011-10-20 20:10:26', '2011-10-20 20:10:26', 2, 2),
(15, 16, 'household goods', 'Outcome', '2011-10-20 20:16:25', '2012-09-09 14:04:58', 2, 1),
(17, 2, 'rent', 'Outcome', '2011-10-20 20:23:24', '2011-10-20 20:23:24', 2, 2),
(18, 2, 'internet', 'Outcome', '2011-10-20 20:26:56', '2011-10-20 20:26:56', 2, 2),
(19, 16, 'repairs', 'Outcome', '2011-10-20 20:30:48', '2011-10-20 20:30:48', 2, 2),
(21, 16, 'tools', 'Outcome', '2011-10-20 20:51:23', '2011-10-20 20:51:23', 2, 2),
(22, 4, 'cinema', 'Outcome', '2011-10-20 21:17:05', '2011-10-20 21:17:05', 2, 2),
(25, 2, 'water', 'Outcome', '2011-10-23 17:42:56', '2011-10-23 17:42:56', 2, 2),
(26, 16, 'flowers', 'Outcome', '2011-10-23 17:45:39', '2011-10-23 17:45:39', 2, 2),
(27, 2, 'gas', 'Outcome', '2011-10-23 17:56:16', '2011-10-23 17:56:16', 2, 2),
(28, 2, 'electricity', 'Outcome', '2011-10-23 17:56:24', '2011-10-23 17:56:24', 2, 2),
(29, 2, 'phones', 'Outcome', '2011-10-23 17:56:33', '2011-10-23 17:56:33', 2, 2),
(30, 49, 'meds', 'Outcome', '2011-10-25 07:00:33', '2012-03-23 10:49:06', 2, 2),
(31, 1, 'meat', 'Outcome', '2011-10-25 07:06:22', '2011-10-25 07:06:22', 2, 2),
(32, 1, 'takeaway', 'Outcome', '2011-10-25 17:38:05', '2011-10-25 17:40:11', 2, 2),
(33, 14, 'cosmetics', 'Outcome', '2011-10-26 17:44:22', '2011-10-26 17:44:22', 2, 2),
(45, 4, 'theatre', 'Outcome', '2012-01-26 17:40:57', '2012-01-26 17:40:57', 2, 2),
(47, 1, 'alcohol', 'Outcome', '2012-02-22 14:27:50', '2012-02-22 14:27:50', 2, 2),
(48, 14, 'barber', 'Outcome', '2012-03-06 23:55:17', '2012-03-06 23:55:17', 1, 1),
(50, 49, 'doctor', 'Outcome', '2012-03-23 10:48:51', '2012-03-23 10:48:51', 2, 2),
(51, 4, 'collectibles', 'Outcome', '2012-03-29 13:10:24', '2012-03-29 13:10:24', 2, 2),
(52, 1, 'fish', 'Outcome', '2012-05-06 12:06:30', '2012-05-06 12:06:30', 2, 2),
(53, 20, 'handout', 'Outcome', '2012-05-13 19:10:11', '2012-05-13 19:10:11', 2, 2),
(55, 20, 'souvenirs', 'Outcome', '2012-08-17 10:36:07', '2012-08-17 10:36:07', 2, 2),
(35, NULL, 'amrs trade', 'Income', '2011-10-26 17:44:22', '2011-10-26 17:44:22', 2, 2),
(37, NULL, 'tribute', 'Income', '2011-10-26 17:44:22', '2011-10-26 17:44:22', 2, 2),
(38, NULL, 'music', 'Income', '2011-10-26 17:44:22', '2011-10-26 17:44:22', 2, 2),
(41, NULL, 'others', 'Income', '2011-11-03 21:31:51', '2012-01-29 18:43:57', 2, 2),
(42, NULL, 'investments', 'Income', '2011-12-06 21:35:25', '2011-12-06 21:35:25', 2, 2),
(36, 35, 'trips', 'Income', '2011-10-26 17:44:22', '2012-01-29 18:44:07', 2, 2),
(39, 38, 'recordings', 'Income', '2011-10-26 17:44:22', '2011-10-26 17:44:22', 2, 2),
(40, 38, 'live shows', 'Income', '2011-10-26 17:44:22', '2011-10-26 17:44:22', 2, 2),
(43, 42, 'gold & silver', 'Income', '2011-12-06 21:35:39', '2011-12-06 21:35:39', 2, 2),
(44, 42, 'debentures', 'Income', '2012-01-02 14:34:32', '2012-01-02 14:34:32', 2, 2),
(46, 35, 'production', 'Income', '2012-01-29 18:41:46', '2012-01-29 18:41:46', 2, 2),
(54, 42, 'real estate', 'Income', '2012-05-25 15:10:21', '2012-05-25 15:10:21', 2, 2);
